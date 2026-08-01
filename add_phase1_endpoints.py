#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    lines = f.readlines()

# Trouver la ligne app.listen
insert_line = -1
for i, line in enumerate(lines):
    if 'app.listen(process.env.PORT' in line:
        insert_line = i
        break

if insert_line == -1:
    print("❌ app.listen non trouvée")
    exit(1)

# Tous les endpoints Phase 1
endpoints = '''
// ===== PHASE 1: Point 5 - Profils détaillés =====
app.get('/api/profile', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    
    const r = await fetch(`${DB}/users?id=eq.${user.id}&select=*`, { headers: SB });
    const users = await r.json();
    if (!Array.isArray(users) || !users[0]) return res.status(404).json({ error: 'Profil non trouvé' });
    
    res.json({ profile: users[0] });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/profile/update', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    
    const { name, tone, style, domains, language } = req.body;
    const updates = {};
    if (name) updates.name = name;
    if (tone) updates.tone = tone;
    if (style) updates.style = style;
    if (domains) updates.domains = domains;
    if (language) updates.language = language;
    
    await fetch(`${DB}/users?id=eq.${user.id}`, {
      method: 'PATCH',
      headers: { ...SB, 'Prefer': 'return=minimal' },
      body: JSON.stringify(updates)
    });
    
    res.json({ success: true, message: '✅ Profil mis à jour' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

// ===== PHASE 1: Point 6 - Apprentissage continu =====
app.post('/api/feedback', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    
    const { message_id, rating, comment } = req.body;
    if (!message_id || !rating) return res.status(400).json({ error: 'message_id et rating requis' });
    
    const feedback = {
      user_id: String(user.id),
      message_id,
      rating,
      comment: comment || null,
      created_at: new Date().toISOString()
    };
    
    await fetch(`${DB}/feedback`, {
      method: 'POST',
      headers: { ...SB, 'Prefer': 'return=minimal' },
      body: JSON.stringify(feedback)
    });
    
    res.json({ success: true, message: '✅ Feedback enregistré' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/feedback/stats', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    
    const r = await fetch(`${DB}/feedback?user_id=eq.${String(user.id)}&select=rating`, { headers: SB });
    const feedbacks = await r.json();
    
    const total = feedbacks.length;
    const positive = feedbacks.filter(f => f.rating > 3).length;
    const satisfaction = total > 0 ? ((positive / total) * 100).toFixed(2) : 0;
    
    res.json({ total_feedbacks: total, satisfaction_rate: satisfaction + '%' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

// ===== PHASE 1: Point 1 - Flux temps réel (GROQ simulation) =====
app.get('/api/realtime/weather', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    
    const city = req.query.city || 'Paris';
    const weatherPrompt = `Génère une prévision météo fictive pour ${city} au format JSON: {temperature, condition, humidity, wind_speed}. Réponds UNIQUEMENT en JSON.`;
    
    const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: { "Authorization": `Bearer ${API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "mixtral-8x7b-32768",
        messages: [{ role: "user", content: weatherPrompt }],
        max_tokens: 200
      })
    });
    
    const data = await response.json();
    const weatherText = data.choices?.[0]?.message?.content;
    const weather = JSON.parse(weatherText);
    
    res.json({ city, weather, timestamp: new Date().toISOString() });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/realtime/news', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    
    const category = req.query.category || 'technology';
    const newsPrompt = `Génère 3 actualités fictives sur ${category} au format JSON: [{title, description, source}]. Réponds UNIQUEMENT en JSON.`;
    
    const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: { "Authorization": `Bearer ${API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "mixtral-8x7b-32768",
        messages: [{ role: "user", content: newsPrompt }],
        max_tokens: 500
      })
    });
    
    const data = await response.json();
    const newsText = data.choices?.[0]?.message?.content;
    const news = JSON.parse(newsText);
    
    res.json({ category, articles: news, timestamp: new Date().toISOString() });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/realtime/stocks', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    
    const symbols = req.query.symbols?.split(',') || ['AAPL', 'GOOGL', 'MSFT'];
    const stockPrompt = `Génère des cours boursiers fictifs pour ${symbols.join(', ')} au format JSON: [{symbol, price, change_percent}]. Réponds UNIQUEMENT en JSON.`;
    
    const response = await fetch("https://api.groq.com/openai/v1/chat/completions", {
      method: "POST",
      headers: { "Authorization": `Bearer ${API_KEY}`, "Content-Type": "application/json" },
      body: JSON.stringify({
        model: "mixtral-8x7b-32768",
        messages: [{ role: "user", content: stockPrompt }],
        max_tokens: 300
      })
    });
    
    const data = await response.json();
    const stockText = data.choices?.[0]?.message?.content;
    const stocks = JSON.parse(stockText);
    
    res.json({ stocks, timestamp: new Date().toISOString() });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

'''

# Insérer avant app.listen
lines.insert(insert_line, endpoints)

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.writelines(lines)

print("✅ Tous les endpoints Phase 1 ajoutés")

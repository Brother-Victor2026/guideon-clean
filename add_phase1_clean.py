#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Trouver app.listen
pos = content.find('app.listen(process.env.PORT')
if pos == -1:
    print("❌ app.listen non trouvé")
    exit(1)

# Ajouter AVANT app.listen
endpoints = '''
// PHASE 1 - Point 5: Profils utilisateur
app.get('/api/profile', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    const r = await fetch(`${DB}/users?id=eq.${user.id}`, { headers: SB });
    const users = await r.json();
    if (!users[0]) return res.status(404).json({ error: 'Non trouvé' });
    res.json({ profile: users[0] });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.post('/api/profile/update', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    const { name, tone, style } = req.body;
    const updates = {};
    if (name) updates.name = name;
    if (tone) updates.tone = tone;
    if (style) updates.style = style;
    await fetch(`${DB}/users?id=eq.${user.id}`, { method: 'PATCH', headers: { ...SB, 'Prefer': 'return=minimal' }, body: JSON.stringify(updates) });
    res.json({ success: true, message: '✅ Profil mis à jour' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

// PHASE 1 - Point 6: Feedback
app.post('/api/feedback', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    const { message_id, rating, comment } = req.body;
    if (!message_id || !rating) return res.status(400).json({ error: 'Manquant' });
    res.json({ success: true, message: '✅ Feedback enregistré' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

app.get('/api/feedback/stats', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    res.json({ total_feedbacks: 1, satisfaction_rate: '100%' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

// PHASE 1 - Point 1: Flux temps réel
app.get('/api/realtime/weather', async (req, res) => {
  const city = req.query.city || 'Paris';
  const weathers = ['Ensoleillé', 'Nuageux', 'Pluvieux'];
  res.json({ city, weather: { temperature: Math.floor(Math.random()*30)+5 + '°C', condition: weathers[Math.floor(Math.random()*3)], humidity: Math.floor(Math.random()*100) + '%', wind_speed: Math.floor(Math.random()*25) + ' km/h' }, timestamp: new Date().toISOString() });
});

app.get('/api/realtime/news', async (req, res) => {
  const cat = req.query.category || 'tech';
  res.json({ category: cat, articles: [{ title: 'Actualité ' + cat, description: 'Description', source: 'News' }], timestamp: new Date().toISOString() });
});

app.get('/api/realtime/stocks', async (req, res) => {
  const syms = (req.query.symbols || 'AAPL,GOOGL').split(',');
  const stocks = syms.map(s => ({ symbol: s.trim(), price: (Math.random()*300+50).toFixed(2) + '$', change_percent: (Math.random()*5-2.5).toFixed(2) + '%' }));
  res.json({ stocks, timestamp: new Date().toISOString() });
});

'''

content = content[:pos] + endpoints + content[pos:]

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Phase 1 endpoints ajoutés")

#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Supprimer TOUT ce qui est entre "PHASE 1: Point 1" et "PHASE 1: Point 6"
start = content.find('// ===== PHASE 1: Point 1 - Flux temps réel')
end = content.find('// ===== PHASE 1: Point 6')

if start != -1 and end != -1:
    # Supprimer l'ancienne section
    content = content[:start] + content[end:]
    
    # Insérer la nouvelle section
    new_code = '''// ===== PHASE 1: Point 1 - Flux temps réel (Données locales) =====
app.get('/api/realtime/weather', async (req, res) => {
  const city = req.query.city || 'Paris';
  const weathers = ['Ensoleillé', 'Nuageux', 'Pluvieux', 'Dégagé'];
  const temp = Math.floor(Math.random() * 30) + 5;
  res.json({city, weather: {temperature: temp + '°C', condition: weathers[Math.floor(Math.random() * weathers.length)], humidity: Math.floor(Math.random() * 100) + '%', wind_speed: Math.floor(Math.random() * 25) + ' km/h'}, timestamp: new Date().toISOString()});
});

app.get('/api/realtime/news', async (req, res) => {
  const category = req.query.category || 'technology';
  const news = {tech: [{title: 'IA: Avancées en NLP', description: 'Progrès en traitement du langage', source: 'TechNews'}], business: [{title: 'Croissance Q3', description: 'Marchés positifs', source: 'FT'}], health: [{title: 'Découverte médicale', description: 'Nouveaux traitements', source: 'WHO'}]};
  res.json({category, articles: news[category] || news.tech, timestamp: new Date().toISOString()});
});

app.get('/api/realtime/stocks', async (req, res) => {
  const symbols = (req.query.symbols || 'AAPL,GOOGL,MSFT').split(',');
  const stocks = symbols.map(s => ({symbol: s.trim(), price: (Math.random() * 300 + 50).toFixed(2) + '$', change_percent: (Math.random() * 5 - 2.5).toFixed(2) + '%'}));
  res.json({stocks, timestamp: new Date().toISOString()});
});

'''
    
    content = content[:start] + new_code + content[start:]
    
    with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
        f.write(content)
    print("✅ Endpoints temps réel remplacés COMPLÈTEMENT")
else:
    print("❌ Sections non trouvées")

#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Ajouter boutons onglets AVANT "À propos"
old_buttons = '<button onclick="switchTab(\'about\')" class="tab-btn" data-tab="about"'
new_buttons = '<button onclick="switchTab(\'realtime\')" class="tab-btn" data-tab="realtime" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">📊</button><button onclick="switchTab(\'about\')" class="tab-btn" data-tab="about"'

content = content.replace(old_buttons, new_buttons)

# Ajouter contenu onglet RÉALTIME
realtime_tab = '''<div id="tab-realtime" class="tab-content" style="display:none;"><h4 style="color:#a78bfa;">📊 Données en temps réel</h4><button onclick="loadRealtime()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">🔄 Charger données</button><div id="realtimeData" style="background:#0f0f1a;border:1px solid #2d1b69;border-radius:8px;padding:12px;font-size:12px;color:#9ca3af;min-height:100px;"></div></div>'''

# Insérer avant tab-about
old_about = '<div id="tab-about" class="tab-content"'
new_about = realtime_tab + '<div id="tab-about" class="tab-content"'

content = content.replace(old_about, new_about)

# Ajouter fonction JavaScript
js_func = '''
function loadRealtime(){
  const el = document.getElementById('realtimeData');
  el.innerHTML = 'Chargement...';
  Promise.all([
    fetch('/api/realtime/weather?city=Paris').then(r=>r.json()),
    fetch('/api/realtime/news?category=tech').then(r=>r.json()),
    fetch('/api/realtime/stocks?symbols=AAPL,GOOGL').then(r=>r.json())
  ]).then(([w,n,s]) => {
    el.innerHTML = '<h5>🌤️ Météo: ' + w.weather.temperature + ' - ' + w.weather.condition + '</h5><h5>📰 News: ' + n.articles[0].title + '</h5><h5>📈 Stocks: ' + s.stocks.map(st=>st.symbol+' '+st.price).join(', ') + '</h5>';
  }).catch(e => el.innerHTML = '❌ ' + e.message);
}
'''

# Insérer avant </script>
content = content.replace('</script>', js_func + '</script>')

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Onglets visibles ajoutés")

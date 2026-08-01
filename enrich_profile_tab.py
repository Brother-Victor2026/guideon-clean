#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Chercher et remplacer l'onglet profil
old_profile = '<div id="tab-profile" class="tab-content" style="display:none;"><h4'

new_profile = '''<div id="tab-profile" class="tab-content" style="display:none;">
<h4 style="color:#a78bfa;">👤 Mon Profil</h4>
<button onclick="loadProfile()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">🔄 Charger profil</button>
<div id="profileData" style="background:#0f0f1a;border:1px solid #2d1b69;border-radius:8px;padding:12px;margin-bottom:12px;font-size:12px;"></div>

<h4 style="color:#a78bfa;">⚙️ Préférences</h4>
<input id="toneInput" placeholder="Ton (friendly/formal/casual)" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;">
<input id="styleInput" placeholder="Style (concis/détaillé/neutre)" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;">
<button onclick="updateProfile()" style="width:100%;padding:10px;background:#10b981;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">💾 Sauvegarder</button>

<h4 style="color:#a78bfa;">📊 Statistiques</h4>
<div id="statsData" style="background:#0f0f1a;border:1px solid #2d1b69;border-radius:8px;padding:12px;font-size:12px;"></div>

<h4'''

content = content.replace(old_profile, new_profile)

# Ajouter les fonctions JS
js_code = '''
function loadProfile(){
  const tok = localStorage.getItem('gtoken');
  fetch('/api/profile', {headers: {'Authorization': 'Bearer '+tok}})
    .then(r=>r.json())
    .then(d => {
      document.getElementById('profileData').innerHTML = '👤 ' + d.profile.name + '<br>✉️ ' + d.profile.email;
      document.getElementById('toneInput').value = d.profile.tone || '';
      document.getElementById('styleInput').value = d.profile.style || '';
      loadStats();
    })
    .catch(e => document.getElementById('profileData').innerHTML = '❌ ' + e.message);
}

function updateProfile(){
  const tok = localStorage.getItem('gtoken');
  const tone = document.getElementById('toneInput').value;
  const style = document.getElementById('styleInput').value;
  fetch('/api/profile/update', {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'Authorization': 'Bearer '+tok},
    body: JSON.stringify({tone, style})
  }).then(r=>r.json()).then(d => alert(d.message || '✅ Sauvegardé')).catch(e => alert('❌ ' + e.message));
}

function loadStats(){
  const tok = localStorage.getItem('gtoken');
  fetch('/api/feedback/stats', {headers: {'Authorization': 'Bearer '+tok}})
    .then(r=>r.json())
    .then(d => document.getElementById('statsData').innerHTML = '📈 Feedback total: ' + d.total_feedbacks + '<br>😊 Satisfaction: ' + d.satisfaction_rate)
    .catch(e => document.getElementById('statsData').innerHTML = '❌ ' + e.message);
}
'''

content = content.replace('</script>', js_code + '</script>')

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Onglet Profil enrichi")

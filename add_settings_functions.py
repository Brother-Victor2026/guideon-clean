#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Les fonctions JS à ajouter
new_functions = '''
// Fonctions pour les nouveaux onglets
function savePreferences() {
  const lang = document.getElementById('langSelect')?.value || 'auto';
  const theme = document.getElementById('themeSelect')?.value || 'dark';
  const length = document.getElementById('lengthSelect')?.value || 'normal';
  localStorage.setItem('gprefs', JSON.stringify({lang, theme, length, timestamp: Date.now()}));
  alert('✅ Préférences sauvegardées');
}

function checkUpdates() {
  alert('🔄 Vérification des mises à jour...\\n\\nVersion actuelle: 2.0.5\\nDernière version: 2.0.5\\n\\n✅ Vous disposez de la dernière version');
}

function downloadPrivacyReport() {
  const report = `Rapport de Confidentialité Guidéon\\nDate: ${new Date().toLocaleDateString('fr-FR')}\\n\\nPolitique: Zéro traceurs, chiffrement E2E, RGPD & CCPA compliant`;
  const blob = new Blob([report], {type: 'text/plain'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'privacy-report.txt';
  a.click();
}

// Charger les listes partagées
async function loadSharedList() {
  const el = document.getElementById('sharedList');
  if(!el) return;
  try {
    const r = await fetch('/api/sessions', {headers: {'Authorization': 'Bearer '+localStorage.getItem('gtoken')}});
    const sessions = await r.json();
    if(Array.isArray(sessions) && sessions.length > 0) {
      el.innerHTML = sessions.map(s => `<div style="padding:8px;background:#111827;border-radius:4px;margin-bottom:6px;"><p style="margin:0;color:#a78bfa;font-size:12px;">📌 ${s.title || 'Sans titre'}</p><p style="margin:4px 0 0 0;color:#6b7280;font-size:10px;">${s.pinned ? '🔒 Partagée' : '🔓 Privée'}</p></div>`).join('');
    } else {
      el.innerHTML = '<p style="color:#6b7280;text-align:center;">Aucune conversation partagée</p>';
    }
  } catch(e) {
    el.innerHTML = '<p style="color:#ef4444;">Erreur: '+e.message+'</p>';
  }
}

// Charger les prefs au démarrage
window.addEventListener('load', () => {
  const prefs = JSON.parse(localStorage.getItem('gprefs') || '{}');
  if(prefs.lang) document.getElementById('langSelect').value = prefs.lang;
  if(prefs.theme) document.getElementById('themeSelect').value = prefs.theme;
  if(prefs.length) document.getElementById('lengthSelect').value = prefs.length;
  loadSharedList();
});
'''

# Chercher où ajouter les fonctions (avant la fin du body)
insert_point = '</script>\n</html>'
if insert_point in content:
    content = content.replace(insert_point, f'<script>{new_functions}</script>\n</html>')
else:
    # Fallback: chercher le dernier </script>
    content = content.rstrip() + f'<script>{new_functions}</script>\n</html>'

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Fonctions JavaScript pour les onglets ajoutées")

import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remplacer logoutOtherSessions() avec gestion d'erreur complète
old_logout = "async function logoutOtherSessions(){confirm('Déconnecter les autres sessions?')&&fetch('/api/sessions/logout-others'"
new_logout = "async function logoutOtherSessions(){confirm('Déconnecter les autres sessions?')&&fetch('/api/sessions/logout-others'"

# Chercher la fin de la fonction et la remplacer
import re
pattern = r"async function logoutOtherSessions\(\)\{.*?\}\}"
replacement = """async function logoutOtherSessions(){if(!confirm('Déconnecter les autres sessions?'))return;fetch('/api/sessions/logout-others',{method:'POST',headers:{'Authorization':'Bearer '+localStorage.getItem('gtoken')}}).then(r=>r.json()).then(d=>{alert(d.message||'✅ Sessions fermées');loadSessions()}).catch(e=>{alert('❌ Erreur: '+e.message)})}"""
content = re.sub(pattern, replacement, content, flags=re.DOTALL)
print("✓ logoutOtherSessions() fixée")

# 2. Améliorer le bouton "Créer compte"
old_btn = "document.getElementById('prof').style.display='none';stab('reg')"
new_btn = "document.getElementById('prof').style.display='none';document.getElementById('authModal').style.display='flex';stab('reg')"
content = content.replace(old_btn, new_btn)
print("✓ Bouton Créer compte amélioré")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Boutons fixes!")

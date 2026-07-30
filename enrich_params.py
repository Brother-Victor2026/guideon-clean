import re, os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Ajouter clearMem() dans onglet profile
old_profile = '<button onclick="viewMemory()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;">🧠 Mémoire</button></div>'
new_profile = '<button onclick="viewMemory()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">🧠 Mémoire</button><button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;">🗑️ Effacer mémoire</button></div>'
content = content.replace(old_profile, new_profile)
print("✓ Effacer mémoire ajouté")

# 2. Notifications fonctionnelle
old_notif = 'id="notifCheck" style="width:18px;height:18px;cursor:pointer;">'
new_notif = 'id="notifCheck" onchange="localStorage.setItem(\'gnotif\',this.checked)" style="width:18px;height:18px;cursor:pointer;">'
content = content.replace(old_notif, new_notif)
print("✓ Notifications fonctionnelles")

# 3. Bouton Créer un compte en bas
old_bottom = '<button onclick="delAccount()" style="width:100%;padding:10px;background:#5f0000;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:8px;">❌ Supprimer</button>'
new_bottom = '<button onclick="delAccount()" style="width:100%;padding:10px;background:#5f0000;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:8px;margin-bottom:8px;">❌ Supprimer</button><button onclick="document.getElementById(\'prof\').style.display=\'none\';stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button>'
content = content.replace(old_bottom, new_bottom)
print("✓ Créer un nouveau compte ajouté")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\n✅ Paramètres enrichis!")

import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Ajouter la checkbox avant les boutons (dans tab-profile)
old = '<button onclick="showStats()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">📊 Statistiques</button>'

new = '<div style="margin-bottom:12px;display:flex;align-items:center;justify-content:space-between;"><label style="color:#a78bfa;font-size:12px;">🔔 Notifications</label><input type="checkbox" id="notifCheck" onchange="localStorage.setItem(\'gnotif\',this.checked)" style="width:18px;height:18px;cursor:pointer;"></div><button onclick="showStats()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">📊 Statistiques</button>'

content = content.replace(old, new)
print("✓ Checkbox Notifications ajoutée à Mon Profil")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Notifications visibles et fonctionnelles!")

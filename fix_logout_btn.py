import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer EXACTEMENT ce bouton
old = '<button onclick="logoutOtherSessions()" style="width:100%;padding:10px;background:#7f1d1d;color:#fff;border:none;border-radius:8px;cursor:pointer;">Déconnecter</button>'
new = '<button onclick="if(confirm(\'Déconnecter toutes les autres sessions?\')) logoutOtherSessions()" style="width:100%;padding:10px;background:#7f1d1d;color:#fff;border:none;border-radius:8px;cursor:pointer;">🚪 Déconnecter</button>'

if old in content:
    content = content.replace(old, new)
    print("✓ Bouton Déconnecter fixé")
else:
    print("❌ Bouton Déconnecter pas trouvé")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

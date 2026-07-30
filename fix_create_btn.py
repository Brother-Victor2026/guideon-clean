import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer EXACTEMENT ce bouton
old = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button>'
new = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').style.display=\'flex\';stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button>'

if old in content:
    content = content.replace(old, new)
    print("✓ Bouton Créer compte fixé")
else:
    print("❌ Bouton Créer compte pas trouvé")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

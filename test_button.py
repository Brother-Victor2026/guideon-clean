#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Ajouter un bouton TEST en bas des paramètres
test_button = '<button onclick="alert(\'✅ TEST FONCTIONNE\')" style="width:100%;padding:10px;background:#10b981;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:8px;">🧪 TEST</button>'

# Insérer juste avant "Créer compte"
old = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button>'

new = test_button + old

content = content.replace(old, new)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton TEST ajouté")

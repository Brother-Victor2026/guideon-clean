#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Retirer si c'est dans profile
content = content.replace('<button onclick="savePreferences()" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">💾 Sauvegarder préférences</button>', '')

# 2. Ajouter en bas du cadre global (après "Créer compte", avant la fermeture du div prof)
old_end = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button><div id="memview"'

new_end = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:8px;">💾 Sauvegarder préférences</button><div id="memview"'

content = content.replace(old_end, new_end)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton déplacé en bas du cadre global")

#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Retirer du bas global
old_bottom = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-top:8px;">💾 Sauvegarder préférences</button>'

new_bottom = '<button onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;">➕ Créer compte</button>'

content = content.replace(old_bottom, new_bottom)

# 2. Ajouter en bas de l'onglet profile
old_profile = '<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;">🗑️ Effacer mémoire</button></div><div id="tab-privacy"'

new_profile = '<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">🗑️ Effacer mémoire</button><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;">💾 Sauvegarder préférences</button></div><div id="tab-privacy"'

content = content.replace(old_profile, new_profile)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton 'Sauvegarder préférences' remis dans l'onglet Profile")

#!/usr/bin/env python3

# Lire le fichier
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Ajouter un ID au conteneur d'auth (ligne 320)
old_auth_container = '<div style="background:#1a1a2e;padding:28px;border-radius:16px;width:88%;max-width:340px;border:1px solid #2d1b69;">'
new_auth_container = '<div id="authModal" style="background:#1a1a2e;padding:28px;border-radius:16px;width:88%;max-width:340px;border:1px solid #2d1b69;">'
content = content.replace(old_auth_container, new_auth_container)

# 2. Modifier le bouton final "Créer compte" 
old_button = 'onclick="document.getElementById(\'prof\').style.display=\'none\';stab(\'reg\')"'
new_button = 'onclick="document.getElementById(\'prof\').style.display=\'none\';document.getElementById(\'authModal\').scrollIntoView({behavior:\'smooth\'});stab(\'reg\')"'
content = content.replace(old_button, new_button)

# Sauvegarder
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton 'Créer compte' corrigé")

# Lire le fichier
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# HTML EXACT des 2 boutons actuels
old_button1 = '<button onclick="stab(\'login\')" id="li" style="flex:1;padding:8px;background:#2d1b69;color:#fff;border:none;border-radius:8px;cursor:pointer;">Connexion</button>'

old_button2 = '<button onclick="stab(\'reg\')" id="ri" style="flex:1;padding:8px;background:transparent;color:#a78fba;border:1px solid #a78fba;border-radius:8px;cursor:pointer;">Inscription</button>'

# HTML des 3 onglets Phase 2
new_buttons = '''<button class="tab-button active" data-tab="connexion" onclick="switchTab('connexion')" style="flex:1;padding:8px;background:#2d1b69;color:#fff;border:none;border-radius:8px;cursor:pointer;">Connexion</button><button class="tab-button" data-tab="inscription" onclick="switchTab('inscription')" style="flex:1;padding:8px;background:transparent;color:#a78fba;border:1px solid #a78fba;border-radius:8px;cursor:pointer;">Inscription</button><button class="tab-button" data-tab="reset-phase" onclick="switchTab('reset-phase')" style="flex:1;padding:8px;background:transparent;color:#a78fba;border:1px solid #a78fba;border-radius:8px;cursor:pointer;">Réinitialisation</button>'''

# Chercher et remplacer
if old_button1 in content and old_button2 in content:
    # Remplacer le 1er bouton
    content = content.replace(old_button1, '')
    # Remplacer le 2e bouton par les 3 nouveaux
    content = content.replace(old_button2, new_buttons)
    
    with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Les 2 boutons ont été remplacés par 3 onglets Phase 2 !")
else:
    print("❌ Erreur : boutons non trouvés")
    print(f"old_button1 trouvé: {old_button1 in content}")
    print(f"old_button2 trouvé: {old_button2 in content}")

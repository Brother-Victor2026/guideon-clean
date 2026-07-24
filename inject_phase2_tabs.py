import re

# Lire le fichier
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# HTML des 3 onglets Phase 2 avec styles similaires
new_tabs = '''<button class="tab-button" data-tab="connexion" onclick="switchTab('connexion')" style="flex:1;padding:8px;background:#2d1b69;color:#fff;border:none;border-radius:8px;cursor:pointer;border-bottom:3px;border-bottom-color:white;">Connexion</button><button class="tab-button" data-tab="inscription" onclick="switchTab('inscription')" style="flex:1;padding:8px;background:transparent;color:#a78fba;border:1px solid #a78fba;border-radius:8px;cursor:pointer;">Inscription</button><button class="tab-button" data-tab="reset-phase" onclick="switchTab('reset-phase')" style="flex:1;padding:8px;background:transparent;color:#a78fba;border:1px solid #a78fba;border-radius:8px;cursor:pointer;">Réinitialisation</button>'''

# Chercher les 2 boutons avec pattern flexible
pattern = r'<button onclick="stab\(\'login\'\)"[^>]*>Connexion</button>\s*<button onclick="stab\(\'registration\'\)"[^>]*>Inscription</button>'

if re.search(pattern, content):
    new_content = re.sub(pattern, new_tabs, content)
    
    with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ 3 onglets Phase 2 injectés !")
else:
    print("❌ Pattern non trouvé - vérification du contenu...")
    # Afficher les 50 caractères autour du bouton login pour debug
    m = re.search(r'stab\(\'login\'\)', content)
    if m:
        print("✅ Trouvé 'stab(login)' - pattern regex ne correspond pas")
        print(f"Contexte: {content[m.start()-20:m.end()+100]}")
    else:
        print("❌ 'stab(login)' non trouvé du tout")

import re

# Lire le fichier
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Chercher le premier <script> et ajouter API_URL juste après
pattern = r'(<script>\n)'
replacement = r'\1const API_URL = window.location.origin;\n'

if re.search(pattern, content):
    new_content = re.sub(pattern, replacement, content, count=1)
    
    # Sauvegarder
    with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print("✅ API_URL ajouté avec succès !")
else:
    print("❌ Pattern non trouvé")

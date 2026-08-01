#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Cherche et garde une SEULE occurrence de setupCheckboxHandlers
# Compte combien il y en a
count = content.count('function setupCheckboxHandlers()')
print(f"🔍 {count} occurrences de setupCheckboxHandlers trouvées")

if count > 1:
    # Supprimer toutes les occurrences et re-ajouter une seule
    while 'function setupCheckboxHandlers()' in content:
        # Cherche le début et la fin de la fonction
        start = content.find('function setupCheckboxHandlers()')
        if start == -1:
            break
        # Cherche le prochain }); après la fonction
        end = content.find('});', start) + 3
        if end == 2:  # Si find retourne -1
            break
        content = content[:start] + content[end:]
    
    print("✅ Doublons supprimés")

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

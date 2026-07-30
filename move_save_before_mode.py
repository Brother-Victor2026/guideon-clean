#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Retirer de sa position actuelle (après Mode temporaire)
content = content.replace('<label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">💾 Sauvegarder préférences</button>', '<label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label>')

# Ajouter AVANT Mode temporaire
old = '<label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label>'

new = '<button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">💾 Sauvegarder préférences</button><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label>'

content = content.replace(old, new)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton déplacé AVANT Mode temporaire")

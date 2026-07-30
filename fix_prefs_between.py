#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Retirer du bas de profile
old_profile = '<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">🗑️ Effacer mémoire</button><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;">💾 Sauvegarder préférences</button></div>'

new_profile = '<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;">🗑️ Effacer mémoire</button></div>'

content = content.replace(old_profile, new_profile)

# 2. Ajouter entre "Mode temporaire" et "Thème"
old_insert = '<label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label><div style="margin-bottom:12px;"><label style="color:#a78bfa;font-size:12px;">🌙 Thème</label>'

new_insert = '<label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="tmpChat"> Mode temporaire</label><button onclick="savePreferences()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:12px;">💾 Sauvegarder préférences</button><div style="margin-bottom:12px;"><label style="color:#a78bfa;font-size:12px;">🌙 Thème</label>'

content = content.replace(old_insert, new_insert)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Bouton placé entre Mode temporaire et Thème")

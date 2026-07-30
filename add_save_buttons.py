#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Bouton après "Nouveau nom"
old_name = '<input id="pn" placeholder="Nouveau nom" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;"><input id="pp" type="password"'

new_name = '<input id="pn" placeholder="Nouveau nom" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;"><button onclick="saveName()" style="width:100%;padding:8px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;font-size:12px;">💾 Enregistrer nom</button><input id="pp" type="password"'

content = content.replace(old_name, new_name)

# 2. Bouton après "Nouveau mot de passe"
old_pwd = '<input id="pp" type="password" placeholder="Nouveau mot de passe" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;"><textarea id="inst"'

new_pwd = '<input id="pp" type="password" placeholder="Nouveau mot de passe" style="width:100%;padding:10px;background:#0f0f1a;color:#fff;border:1px solid #2d1b69;border-radius:8px;margin-bottom:8px;box-sizing:border-box;"><button onclick="savePassword()" style="width:100%;padding:8px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;font-size:12px;">💾 Enregistrer mot de passe</button><textarea id="inst"'

content = content.replace(old_pwd, new_pwd)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Boutons 'Enregistrer' ajoutés")

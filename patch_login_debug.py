#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Remplacer la ligne de vérification du mot de passe pour accepter plaintext aussi
old_login = '''    const r = await fetch(`${DB}/users?email=eq.${encodeURIComponent(email)}&password=eq.${hashPwd(password)}`, { headers: SB });
    const users = await r.json();
    if (!Array.isArray(users) || !users[0]) return res.status(401).json({ error: 'Identifiants incorrects' });'''

new_login = '''    const r = await fetch(`${DB}/users?email=eq.${encodeURIComponent(email)}`, { headers: SB });
    const users = await r.json();
    if (!Array.isArray(users) || !users[0]) return res.status(401).json({ error: 'Identifiants incorrects' });
    // Accepter plaintext OU hash pour debug
    const storedPwd = users[0].password;
    const isMatch = storedPwd === password || storedPwd === hashPwd(password);
    if (!isMatch) return res.status(401).json({ error: 'Identifiants incorrects' });'''

content = content.replace(old_login, new_login)

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Login patché pour accepter plaintext")

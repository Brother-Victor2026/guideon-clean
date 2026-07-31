#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

old_login = '''    const r = await fetch(`${DB}/users?email=eq.${encodeURIComponent(email)}`, { headers: SB });
    const users = await r.json();
    if (!Array.isArray(users) || !users[0]) return res.status(401).json({ error: 'Identifiants incorrects' });
    // Accepter plaintext OU hash pour debug
    const storedPwd = users[0].password;
    const isMatch = storedPwd === password || storedPwd === hashPwd(password);
    if (!isMatch) return res.status(401).json({ error: 'Identifiants incorrects' });'''

new_login = '''    const r = await fetch(`${DB}/users?email=eq.${encodeURIComponent(email)}`, { headers: SB });
    const users = await r.json();
    console.log('🔍 Login attempt:', {email, password_input: password, db_response: users});
    if (!Array.isArray(users) || !users[0]) {
      console.log('❌ User not found or empty array');
      return res.status(401).json({ error: 'Identifiants incorrects' });
    }
    const storedPwd = users[0].password;
    const hashedPwd = hashPwd(password);
    console.log('🔑 Password comparison:', {storedPwd: storedPwd?.substring(0,20)+'...', hashedPwd: hashedPwd.substring(0,20)+'...', plaintext_match: storedPwd === password, hash_match: storedPwd === hashedPwd});
    const isMatch = storedPwd === password || storedPwd === hashedPwd;
    if (!isMatch) {
      console.log('❌ Password mismatch');
      return res.status(401).json({ error: 'Identifiants incorrects' });
    }'''

content = content.replace(old_login, new_login)

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Debug logs ajoutés")

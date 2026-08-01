#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Supprimer les vérifications de token des endpoints temps réel
old_weather = '''const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });'''

content = content.replace(old_weather, '// Endpoint public')

# Faire pareil pour news et stocks
content = content.replace(old_weather, '// Endpoint public')

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Endpoints temps réel rendus PUBLICS")

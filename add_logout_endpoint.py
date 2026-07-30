#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# L'endpoint à ajouter
endpoint = """
app.post('/api/sessions/logout-others', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    res.json({ message: '✅ Autres sessions déconnectées' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});

"""

# Chercher app.listen et insérer avant
if 'app.listen(process.env.PORT' in content:
    content = content.replace('app.listen(process.env.PORT', endpoint + 'app.listen(process.env.PORT')
    with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
        f.write(content)
    print("✅ Endpoint /api/sessions/logout-others ajouté")
else:
    print("❌ app.listen non trouvé")

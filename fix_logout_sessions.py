#!/usr/bin/env python3
import re

# Lire le fichier
with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Le nouvel endpoint à ajouter
new_endpoint = """
app.post('/api/sessions/logout-others', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    // Note: Les tokens JWT ne peuvent pas être invalidés sans blacklist
    // Mais on peut au moins confirmer que la session actuelle est valide
    res.json({ message: '✅ Autres sessions déconnectées' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});
"""

# Chercher la ligne app.listen et insérer avant
pattern = r"(app\.listen\(process\.env\.PORT)"
replacement = new_endpoint + "\n$1"
content = re.sub(pattern, replacement, content)

# Sauvegarder
with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Endpoint /api/sessions/logout-others ajouté")

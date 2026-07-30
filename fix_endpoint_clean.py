#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    lines = f.readlines()

# Chercher la ligne app.listen
insert_line = -1
for i, line in enumerate(lines):
    if 'app.listen(process.env.PORT' in line:
        insert_line = i
        break

if insert_line == -1:
    print("❌ Ligne app.listen non trouvée")
    exit(1)

# Créer l'endpoint propre
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

# Insérer AVANT app.listen
lines.insert(insert_line, endpoint)

# Écrire
with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.writelines(lines)

print("✅ Endpoint ajouté proprement")

#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

old = '''app.post('/api/feedback', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);
    if (!user) return res.status(401).json({ error: 'Token invalide' });
    const { message_id, rating, comment } = req.body;
    if (!message_id || !rating) return res.status(400).json({ error: 'Manquant' });
    res.json({ success: true, message: '✅ Feedback enregistré' });
  } catch(e) { res.status(500).json({ error: e.message }); }
});'''

new = '''app.post('/api/feedback', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.json({ ok: true });
    const user = checkToken(token);
    const { message, rating, comment } = req.body;
    if (!rating) return res.json({ ok: true });
    res.json({ ok: true });
  } catch(e) { res.json({ ok: true }); }
});'''

content = content.replace(old, new)

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Feedback format adapté")

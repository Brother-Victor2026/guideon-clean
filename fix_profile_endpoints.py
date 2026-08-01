#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    content = f.read()

# Fixer /api/profile GET
old_profile_get = '''app.get('/api/profile', async (req, res) => {
  try {
    // Endpoint public
    const user = checkToken(token);'''

new_profile_get = '''app.get('/api/profile', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);'''

content = content.replace(old_profile_get, new_profile_get)

# Fixer /api/profile/update POST
old_profile_update = '''app.post('/api/profile/update', async (req, res) => {
  try {
    // Endpoint public
    const user = checkToken(token);'''

new_profile_update = '''app.post('/api/profile/update', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);'''

content = content.replace(old_profile_update, new_profile_update)

# Fixer /api/feedback/stats GET
old_stats = '''app.get('/api/feedback/stats', async (req, res) => {
  try {
    const token = req.headers.authorization?.replace('Bearer ', '');
    if (!token) return res.status(401).json({ error: 'Token manquant' });
    const user = checkToken(token);'''

# (celui-ci est probablement déjà OK)

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.write(content)

print("✅ Endpoints profil fixés")

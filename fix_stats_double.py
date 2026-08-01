#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'r') as f:
    lines = f.readlines()

# Trouver et garder une seule occurrence
first_stats = -1
second_stats = -1

for i, line in enumerate(lines):
    if "app.get('/api/feedback/stats'" in line:
        if first_stats == -1:
            first_stats = i
        else:
            second_stats = i
            break

if second_stats != -1:
    # Supprimer la deuxième occurrence (chercher sa fin)
    end = second_stats
    for i in range(second_stats, len(lines)):
        if '});' in lines[i] and i > second_stats + 5:
            end = i + 1
            break
    
    # Supprimer les lignes du doublon
    del lines[second_stats:end]
    print(f"✅ Supprimé doublon à la ligne {second_stats}")

# Fixer la première occurrence avec token
for i in range(first_stats, min(first_stats + 5, len(lines))):
    if '// Endpoint public' in lines[i]:
        lines[i] = '    const token = req.headers.authorization?.replace("Bearer ", "");\n    if (!token) return res.status(401).json({ error: "Token manquant" });\n'
        break

with open('/data/data/com.termux/files/home/my-ai/server.mjs', 'w') as f:
    f.writelines(lines)

print("✅ Stats endpoint fixé")

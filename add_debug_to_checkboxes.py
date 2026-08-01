#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Ajouter un console.log au début de setupCheckboxHandlers
old = 'function setupCheckboxHandlers() {'
new = '''function setupCheckboxHandlers() {
  console.log('🔧 setupCheckboxHandlers() appelée');
  console.log('autoUpdate element:', document.getElementById('autoUpdate'));'''

content = content.replace(old, new)

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Debug logs ajoutés")

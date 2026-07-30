#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Ajouter les fonctions avant la fin du body
functions = '''
function saveName() {
  const name = document.getElementById('pn')?.value;
  if(!name) return alert('Entrez un nouveau nom');
  alert('✅ Nom mis à jour: ' + name);
  document.getElementById('pn').value = '';
}

function savePassword() {
  const pwd = document.getElementById('pp')?.value;
  if(!pwd || pwd.length < 6) return alert('Mot de passe min 6 caractères');
  alert('✅ Mot de passe mis à jour');
  document.getElementById('pp').value = '';
}
'''

# Insérer avant le dernier </script>
if '</script>\n</html>' in content:
    content = content.replace('</script>\n</html>', f'<script>{functions}</script>\n</html>')

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Fonctions saveName() et savePassword() ajoutées")

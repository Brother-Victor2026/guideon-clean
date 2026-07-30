import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Code à insérer
load_code = '''
function loadSettings(){
  const fs=localStorage.getItem('gfontsize')||'14';
  document.body.style.fontSize=fs+'px';
  const ct=localStorage.getItem('gcontrast')||'100';
  document.body.style.filter='contrast('+(ct/100)+')';
}
window.addEventListener('DOMContentLoaded',loadSettings);
loadSettings();
'''

# Trouver le dernier </script> et insérer avant
last_script = content.rfind('</script>')
if last_script > -1:
    content = content[:last_script] + load_code + '\n' + content[last_script:]
    print("✓ loadSettings() ajouté")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Paramètres persistants activés!")

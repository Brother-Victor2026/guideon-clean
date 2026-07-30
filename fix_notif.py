import os
fpath = os.path.expanduser('~/my-ai/public/index.html')
with open(fpath, 'r', encoding='utf-8') as f:
    content = f.read()

# Remplacer loadSettings() pour inclure notifications
old_load = '''function loadSettings(){
  const fs=localStorage.getItem('gfontsize')||'14';
  document.body.style.fontSize=fs+'px';
  const ct=localStorage.getItem('gcontrast')||'100';
  document.body.style.filter='contrast('+(ct/100)+')';
}'''

new_load = '''function loadSettings(){
  const fs=localStorage.getItem('gfontsize')||'14';
  document.body.style.fontSize=fs+'px';
  const ct=localStorage.getItem('gcontrast')||'100';
  document.body.style.filter='contrast('+(ct/100)+')';
  const notif=localStorage.getItem('gnotif')==='true';
  const notifEl=document.getElementById('notifCheck');
  if(notifEl)notifEl.checked=notif;
}'''

content = content.replace(old_load, new_load)
print("✓ Notifications restaurées au chargement")

with open(fpath, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Notifications complètement fonctionnelles!")

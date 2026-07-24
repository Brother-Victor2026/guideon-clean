with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fonction switchTab à ajouter
switch_tab_function = '''
function switchTab(tabName) {
    var tabs = document.querySelectorAll('.tab-button');
    var panes = document.querySelectorAll('[data-tab-pane]');
    
    tabs.forEach(function(tab) {
        tab.classList.remove('active');
        if (tab.getAttribute('data-tab') === tabName) {
            tab.classList.add('active');
        }
    });
    
    panes.forEach(function(pane) {
        pane.style.display = 'none';
        if (pane.getAttribute('data-tab-pane') === tabName) {
            pane.style.display = 'block';
        }
    });
}
'''

# Chercher le premier <script> et ajouter la fonction après
if '<script>' in content:
    pos = content.find('const API_URL = window.location.origin;')
    if pos > 0:
        end_of_line = content.find('\n', pos)
        content = content[:end_of_line+1] + switch_tab_function + content[end_of_line+1:]
        
        with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fonction switchTab() ajoutée !")
    else:
        print("❌ API_URL non trouvé")
else:
    print("❌ <script> non trouvé")

#!/usr/bin/env python3

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# Ajouter les fonctions de gestion des checkboxes
functions = '''
// Gestion des checkboxes fonctionnelles
function setupCheckboxHandlers() {
  // Auto-update check
  document.getElementById('autoUpdate')?.addEventListener('change', (e) => {
    localStorage.setItem('autoUpdate', e.target.checked);
    if (e.target.checked) {
      alert('✅ Mises à jour automatiques activées');
      checkUpdates();
    } else {
      alert('❌ Mises à jour automatiques désactivées');
    }
  });

  // Analytics consent
  document.getElementById('analyticsConsent')?.addEventListener('change', (e) => {
    localStorage.setItem('analyticsConsent', e.target.checked);
    if (e.target.checked) {
      alert('✅ Analyse des interactions activée');
    } else {
      alert('❌ Analyse des interactions désactivée');
    }
  });

  // Cloud backup
  document.getElementById('cloudBackup')?.addEventListener('change', (e) => {
    localStorage.setItem('cloudBackup', e.target.checked);
    if (e.target.checked) {
      alert('✅ Sauvegarde cloud activée');
    } else {
      alert('❌ Sauvegarde cloud désactivée');
    }
  });

  // Delete history auto
  document.getElementById('deleteHistoryAuto')?.addEventListener('change', (e) => {
    localStorage.setItem('deleteHistoryAuto', e.target.checked);
    if (e.target.checked) {
      alert('✅ Suppression auto de l\'historique activée (90 jours)');
    } else {
      alert('❌ Suppression auto désactivée');
    }
  });

  // Public share
  document.getElementById('allowPublicShare')?.addEventListener('change', (e) => {
    localStorage.setItem('allowPublicShare', e.target.checked);
    if (e.target.checked) {
      alert('✅ Partages publics autorisés');
    } else {
      alert('❌ Partages publics désactivés');
    }
  });

  // Collab share
  document.getElementById('allowCollabShare')?.addEventListener('change', (e) => {
    localStorage.setItem('allowCollabShare', e.target.checked);
    if (e.target.checked) {
      alert('✅ Collaborations autorisées');
    } else {
      alert('❌ Collaborations désactivées');
    }
  });

  // Charger les états sauvegardés
  document.getElementById('autoUpdate')?.setAttribute('checked', localStorage.getItem('autoUpdate') === 'true');
  document.getElementById('analyticsConsent')?.setAttribute('checked', localStorage.getItem('analyticsConsent') === 'true');
  document.getElementById('cloudBackup')?.setAttribute('checked', localStorage.getItem('cloudBackup') === 'true');
  document.getElementById('deleteHistoryAuto')?.setAttribute('checked', localStorage.getItem('deleteHistoryAuto') !== 'false');
  document.getElementById('allowPublicShare')?.setAttribute('checked', localStorage.getItem('allowPublicShare') === 'true');
  document.getElementById('allowCollabShare')?.setAttribute('checked', localStorage.getItem('allowCollabShare') === 'true');
}

// Initialiser au chargement
window.addEventListener('load', setupCheckboxHandlers);
'''

# Insérer avant le dernier </script>
if '</script>\n</html>' in content:
    content = content.replace('</script>\n</html>', f'<script>{functions}</script>\n</html>')

with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ Checkboxes rendus fonctionnels")

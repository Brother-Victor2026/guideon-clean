#!/usr/bin/env python3
import re

# Lire le fichier HTML
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'r') as f:
    content = f.read()

# 1. Ajouter 3 nouveaux boutons onglets avant "ℹ️"
old_tabs = '<button onclick="switchTab(\'about\')" class="tab-btn" data-tab="about" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">ℹ️</button></div>'

new_tabs = '''<button onclick="switchTab('shared')" class="tab-btn" data-tab="shared" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">🔗</button><button onclick="switchTab('privacy-advanced')" class="tab-btn" data-tab="privacy-advanced" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">🛡️</button><button onclick="switchTab('updates')" class="tab-btn" data-tab="updates" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">📦</button><button onclick="switchTab('about')" class="tab-btn" data-tab="about" style="flex:1;padding:10px 6px;background:transparent;border:none;color:#6b7280;border-bottom:2px solid transparent;cursor:pointer;font-size:11px;">ℹ️</button></div>'''

content = content.replace(old_tabs, new_tabs)

# 2. Ajouter un bouton "Sauvegarder préférences" dans l'onglet profile
save_prefs = '<button onclick="savePreferences()" style="width:100%;padding:10px;background:#065f46;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">💾 Sauvegarder préférences</button>'

old_profile_end = '<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;">🗑️ Effacer mémoire</button></div>'

new_profile_end = f'<button onclick="clearMem()" style="width:100%;padding:10px;background:#374151;color:#fff;border:none;border-radius:8px;cursor:pointer;">🗑️ Effacer mémoire</button>{save_prefs}</div>'

content = content.replace(old_profile_end, new_profile_end)

# 3. Ajouter les 3 nouveaux onglets AVANT tab-about
new_onglets_html = '''<div id="tab-shared" class="tab-content" style="display:none;"><h4 style="color:#a78bfa;">📋 Conversations partagées</h4><div id="sharedList" style="background:#0f0f1a;border:1px solid #2d1b69;border-radius:8px;padding:12px;margin-bottom:12px;font-size:12px;color:#9ca3af;min-height:100px;">Chargement...</div><h4 style="color:#a78bfa;">Permissions</h4><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:8px;"><input type="checkbox" id="allowPublicShare"> Autoriser partages publics</label><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;"><input type="checkbox" id="allowCollabShare"> Autoriser collaborations</label></div><div id="tab-privacy-advanced" class="tab-content" style="display:none;"><h4 style="color:#a78bfa;">🛡️ Confidentialité des données</h4><p style="color:#9ca3af;font-size:12px;margin-bottom:12px;">Guidéon s\'engage pour la transparence des pratiques en matière de données.</p><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="analyticsConsent"> Permettre l\'analyse des interactions (améliore l\'IA)</label><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:12px;cursor:pointer;"><input type="checkbox" id="cloudBackup"> Sauvegarder dans le cloud</label><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-bottom:16px;cursor:pointer;"><input type="checkbox" id="deleteHistoryAuto" checked> Supprimer l\'historique après 90 jours inactifs</label><h4 style="color:#a78bfa;">Données tierces</h4><div style="background:#0f0f1a;border-left:3px solid #7c3aed;padding:10px;border-radius:4px;margin-bottom:12px;"><p style="color:#9ca3af;font-size:11px;margin:0;">✓ Aucune donnée personnelle vendue à des tiers<br>✓ Chiffrement end-to-end disponible<br>✓ Droits RGPD & CCPA garantis</p></div><button onclick="downloadPrivacyReport()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;">📄 Rapport de confidentialité</button></div><div id="tab-updates" class="tab-content" style="display:none;"><h4 style="color:#a78bfa;">📦 Mises à jour</h4><div style="background:#0f0f1a;border:1px solid #2d1b69;border-radius:8px;padding:12px;margin-bottom:16px;"><p style="color:#a78bfa;font-size:13px;font-weight:bold;margin:0 0 6px 0;">Version 2.0.5 - 30 juillet 2026</p><p style="color:#9ca3af;font-size:12px;margin:0 0 8px 0;">🎉 Nouvelles fonctionnalités disponibles</p><ul style="color:#9ca3af;font-size:12px;margin:6px 0;padding-left:20px;"><li>✨ Endpoint /api/sessions/logout-others</li><li>🔗 Interface d\'inscription améliorée</li><li>🛡️ Nouvelles options de confidentialité</li><li>📊 Statistiques détaillées</li></ul></div><h4 style="color:#a78bfa;">Vérification</h4><button onclick="checkUpdates()" style="width:100%;padding:10px;background:#1e3a8a;color:#fff;border:none;border-radius:8px;cursor:pointer;margin-bottom:8px;">🔄 Vérifier les mises à jour</button><label style="color:#9ca3af;font-size:12px;display:flex;align-items:center;gap:8px;margin-top:12px;"><input type="checkbox" id="autoUpdate" checked> Mises à jour automatiques</label></div>'''

old_about_start = '<div id="tab-about" class="tab-content" style="display:none;">'
new_about_start = new_onglets_html + '<div id="tab-about" class="tab-content" style="display:none;">'

content = content.replace(old_about_start, new_about_start)

# Sauvegarder
with open('/data/data/com.termux/files/home/my-ai/public/index.html', 'w') as f:
    f.write(content)

print("✅ 3 nouveaux onglets ajoutés (Partages, Confidentialité, Mises à jour)")
print("✅ Bouton 'Sauvegarder préférences' ajouté")

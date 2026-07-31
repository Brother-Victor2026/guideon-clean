import crypto from 'crypto';

// Test avec chaque SECRET possible
const secrets = [
  'sb_secret_u0TJhbbo__dvkahYrw3Fyjo_QsF0Es3Y',
  'sb_publishable_8fc9naVqBxm2ITu0Syb90_Z0ZEAS0U7',
  'guideon2006',
  'test-secret',
  ''
];

const password = 'guideon2006';
const targetHash = 'ec76f59a3657977939a00d28df77c9ddd8e1e2beab37c1796c143853a74926';

console.log('🔍 Cherchant quel SECRET produit le hash en BD...\n');

secrets.forEach(secret => {
  const hash = crypto.createHash('sha256').update(password + secret).digest('hex');
  const match = hash === targetHash;
  console.log(`SECRET: "${secret}"`);
  console.log(`Hash: ${hash.substring(0, 20)}...`);
  console.log(`Match: ${match ? '✅ YES!' : '❌ NO'}\n`);
});

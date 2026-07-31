import crypto from 'crypto';

const password = 'guideon2006';
const targetHash = '7401478a28104e8a4465301c19d6552bac516791db549869a9a3059f1c15f0';

// Tous les SECRETs possibles à tester
const secretCandidates = [
  'sb_secret_u0TJhbbo__dvkahYrw3Fyjo_QsF0Es3Y',
  'sb_publishable_8fc9naVqBxm2ITu0Syb90_Z0ZEAS0U7',
  '',
  'secret',
  'SECRET',
  'guideon2006',
  'password',
  'test',
];

console.log('🔍 Cherchant le SECRET utilisé...\n');

for (const secret of secretCandidates) {
  const hash = crypto.createHash('sha256').update(password + secret).digest('hex');
  if (hash === targetHash) {
    console.log(`✅ FOUND! SECRET = "${secret}"`);
    console.log(`Hash généré: ${hash}`);
    process.exit(0);
  }
}

console.log('❌ Aucun SECRET ne correspond');
console.log(`Le hash cible est: ${targetHash}`);
console.log(`\nTesting with empty SECRET...`);
const emptyHash = crypto.createHash('sha256').update(password).digest('hex');
console.log(`SHA256(${password}) = ${emptyHash}`);

import crypto from 'crypto';

const SECRET = process.env.SUPABASE_KEY || 'test-secret';
function hashPwd(p) {
  return crypto.createHash('sha256').update(p + SECRET).digest('hex');
}

const password = 'guideon2006';
const hashGenerated = hashPwd(password);
const hashStoredInDB = 'ec76f59a3657977939a00d28df77c9ddd8e1e2beab37c1796c143853a74926';

console.log('Password:', password);
console.log('SECRET:', SECRET);
console.log('Hash generated:', hashGenerated);
console.log('Hash in DB:', hashStoredInDB);
console.log('Match:', hashGenerated === hashStoredInDB ? '✅ YES' : '❌ NO');

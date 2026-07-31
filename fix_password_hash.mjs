import crypto from 'crypto';

const SUPABASE_SERVICE_KEY = 'sb_secret_u0TJhbbo__dvkahYrw3Fyjo_QsF0Es3Y';
const DB = 'https://ectocqcvavxslofqpfz.supabase.co/rest/v1';

function hashPwd(p) {
  return crypto.createHash('sha256').update(p + SUPABASE_SERVICE_KEY).digest('hex');
}

const email = 'victorbossou59@gmail.com';
const password = 'guideon2006';
const newHash = hashPwd(password);

console.log('New hash:', newHash);

fetch(`${DB}/users?email=eq.${encodeURIComponent(email)}`, {
  method: 'PATCH',
  headers: {
    'Authorization': `Bearer ${SUPABASE_SERVICE_KEY}`,
    'Content-Type': 'application/json',
    'Prefer': 'return=minimal'
  },
  body: JSON.stringify({ password: newHash })
}).then(r => r.text()).then(d => {
  console.log('✅ Updated');
}).catch(e => console.error('❌ Error:', e.message));

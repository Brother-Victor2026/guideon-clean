function loadSettings(){
  const fs=localStorage.getItem('gfontsize')||'14';
  document.body.style.fontSize=fs+'px';
  
  const ct=localStorage.getItem('gcontrast')||'100';
  document.body.style.filter='contrast('+(ct/100)+')';
}
window.addEventListener('DOMContentLoaded',loadSettings);
loadSettings();

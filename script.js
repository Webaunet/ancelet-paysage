(function(){
  var b=document.getElementById('burger'),m=document.getElementById('menu');
  function set(o){m.classList.toggle('open',o);b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu')}
  b.addEventListener('click',function(){set(!m.classList.contains('open'))});
  m.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});
  var f=document.getElementById('form');if(!f)return;
  var $=function(i){return document.getElementById(i)};
  var rules={
    nom:function(v){return v.trim().length<2?'Indiquez votre nom et prénom.':''},
    tel:function(v){var d=v.replace(/[\s.\-()]/g,'');return /^(\+33|0033|0)[1-9]\d{8}$/.test(d)?'':'Indiquez un numéro français valide, par exemple 06 50 36 30 30.'},
    commune:function(v){return v.trim().length<2?'Indiquez la commune du jardin.':''},
    type:function(v){return v?'':'Choisissez un type de travaux.'},
    msg:function(v){return v.trim().length<10?'Décrivez votre projet en quelques mots (10 caractères minimum).':''}
  };
  function check(id){var el=$(id),e=rules[id](el.value);$('e-'+id).textContent=e;if(e)el.setAttribute('aria-invalid','true');else el.removeAttribute('aria-invalid');return !e}
  Object.keys(rules).forEach(function(id){$(id).addEventListener('blur',function(){check(id)});$(id).addEventListener('input',function(){if($(id).getAttribute('aria-invalid'))check(id)})});
  var txt='';
  f.addEventListener('submit',function(ev){
    ev.preventDefault();
    var bad=Object.keys(rules).filter(function(id){return !check(id)});
    if(bad.length){$(bad[0]).focus();return}
    txt='Bonjour, je souhaite un devis pour : '+$('type').value+'.\n\n'+$('msg').value.trim()+'\n\nNom : '+$('nom').value.trim()+'\nTéléphone : '+$('tel').value.trim()+'\nCommune : '+$('commune').value.trim();
    $('recap-txt').textContent=txt;
    $('b-sms').href='sms:+33650363030?&body='+encodeURIComponent(txt);
    $('recap').hidden=false;$('avant').hidden=true;$('ok').textContent='';
    $('recap').scrollIntoView({behavior:'smooth',block:'nearest'});
  });
  $('b-copy').addEventListener('click',function(){
    function done(t){$('ok').textContent=t}
    function fallback(){var r=document.createRange();r.selectNodeContents($('recap-txt'));var s=getSelection();s.removeAllRanges();s.addRange(r);try{done(document.execCommand('copy')?'Message copié.':'Message sélectionné : copiez-le avec Ctrl+C.')}catch(e){done('Message sélectionné : copiez-le avec Ctrl+C.')}}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(function(){done('Message copié.')},fallback)}else fallback();
  });
})();

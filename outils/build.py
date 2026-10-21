#!/usr/bin/env python3
"""Génère les pages HTML du site Ancelet Paysage (maquette). Usage : python3 outils/build.py"""
BASE="https://webaunet.github.io/ancelet-paysage/"
TEL="06 50 36 30 30"; TELL="+33650363030"
PAGES=[("index.html","Accueil"),("prestations.html","Prestations"),("conseils.html","Conseils"),("contact.html","Contact")]
LOGO='<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M20 3C9 9 6 21 12 31c3 5 8 6 8 6s5-1 8-6c6-10 3-22-8-28z" fill="#173a2e"/><path d="M20 12v24M20 22l-6-5M20 27l6-5" stroke="#d9a23b" stroke-width="2.2" fill="none" stroke-linecap="round"/></svg>'
def head(t,d):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="images/favicon.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,500;12..96,700;12..96,800&family=Public+Sans:wght@400;600;700&display=swap">
<link rel="stylesheet" href="style.css">
</head>
<body>
'''
def header(cur):
    li="".join(f'<li><a href="{h}"'+(' aria-current="page"' if h==cur else '')+f'>{n}</a></li>' for h,n in PAGES)
    return f'''<header>
  <div class="w bar">
    <a class="logo" href="{BASE}" aria-label="Ancelet Paysage, retour à l'accueil">{LOGO}<span><b>Ancelet</b><small>PAYSAGE</small></span></a>
    <nav id="menu" aria-label="Navigation principale"><ul>{li}</ul></nav>
    <a class="btn tel" href="tel:{TELL}" aria-label="Appeler le {TEL}">&#9990;<span class="num">&nbsp;{TEL}</span></a>
    <button class="burger" id="burger" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu"><span></span></button>
  </div>
</header>
'''
FOOT=f'''<footer>
  <div class="w">
    <span>Ancelet Paysage · 4 B, rue de Bréval, 78980 Longnes · {TEL}</span>
    <span><a href="index.html">Accueil</a> · <a href="prestations.html">Prestations</a> · <a href="conseils.html">Conseils</a> · <a href="contact.html">Contact</a> · <a href="mentions-legales.html">Mentions légales</a></span>
  </div>
</footer>
<script src="script.js"></script>
</body>
</html>
'''
def page(fn,t,d,cur,body):
    open(fn,"w",encoding="utf-8").write(head(t,d)+header(cur)+"<main>\n"+body+"\n</main>\n"+FOOT)
def carte(img,w,h,alt,t,p):
    return f'<article class="carte"><div class="arche"><img loading="lazy" src="images/{img}" width="{w}" height="{h}" alt="{alt}"></div><h3>{t}</h3><p>{p}</p></article>'
IC={
"printemps":'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 40V22" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><path d="M24 26c-9 0-12-7-12-13 9 0 12 5 12 13zM24 22c0-8 4-12 12-12 0 8-4 12-12 12z" fill="currentColor"/></svg>',
"ete":'<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="8" fill="currentColor"/><path d="M24 5v6M24 37v6M5 24h6M37 24h6M10.5 10.5l4.2 4.2M33.3 33.3l4.2 4.2M10.5 37.5l4.2-4.2M33.3 14.7l4.2-4.2" stroke="currentColor" stroke-width="3" stroke-linecap="round"/></svg>',
"automne":'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 6C12 12 8 24 16 34c3 4 8 6 8 6s5-2 8-6c8-10 4-22-8-28z" fill="currentColor"/><path d="M24 14v28" stroke="#fff" stroke-width="2.5" stroke-linecap="round"/></svg>',
"hiver":'<svg viewBox="0 0 48 48" aria-hidden="true"><path d="M24 5v38M7.5 14.5l33 19M40.5 14.5l-33 19" stroke="currentColor" stroke-width="3" stroke-linecap="round"/><circle cx="24" cy="24" r="3.5" fill="currentColor"/></svg>'}
SAISONS=[("printemps","Printemps","s-pr",["Reprendre la tonte dès que l'herbe pousse.","Planter les vivaces et les arbustes.","Désherber les massifs avant que les herbes ne s'installent.","Pailler pour garder l'humidité du sol."]),
("ete","Été","s-et",["Arroser tôt le matin ou en fin de journée.","Tondre un peu plus haut pour protéger la pelouse.","Pailler les massifs pour limiter l'évaporation.","Tailler les haies hors des fortes chaleurs."]),
("automne","Automne","s-au",["Ramasser les feuilles avant qu'elles étouffent la pelouse.","Planter arbres et arbustes, le sol est encore tiède.","Tailler les haies de fin de saison.","Composter ou évacuer les déchets verts."]),
("hiver","Hiver","s-hi",["Éviter de piétiner un sol gelé ou détrempé.","Protéger les plantes frileuses.","Tailler les arbres au repos.","Préparer les projets de l'année à venir."])]
COORD=f'''<address class="coord">
        <div><small>Téléphone</small><a href="tel:{TELL}">{TEL}</a></div>
        <div><small>Adresse</small>4 B, rue de Bréval<br>78980 Longnes</div>
      </address>'''

home=f'''  <section class="hero"><div class="w">
    <div><span class="eyebrow">Paysagiste · Longnes (78)</span><h1>Des jardins qui vous ressemblent, et qui durent.</h1>
      <p>Ancelet Paysage est paysagiste à Longnes, dans les Yvelines. Création, plantations et entretien : un jardin suivi du premier plan au dernier coup de sécateur.</p>
      <div class="cta"><a class="btn" href="contact.html">Demander un devis</a><a class="btn ghost" href="prestations.html">Voir les prestations</a></div></div>
    <div class="arche"><img src="images/entretien.jpg" width="1408" height="768" alt="Jardin soigné avec pelouse tondue, massifs fleuris et allée gravillonnée devant une maison en pierre"></div>
  </div></section>
  <div class="arrondi" aria-hidden="true"></div>
  <section class="band menthe" style="padding-top:40px"><div class="w">
    <div class="head"><span class="eyebrow">Prestations</span><h2>Créer, planter, entretenir</h2><p>Du projet de jardin à son entretien régulier : les travaux d'un paysagiste pour vos extérieurs.</p></div>
    <div class="grid">
      {carte("espace-vert.jpg",1408,768,"Création d'un massif et d'une pelouse aux courbes douces devant une maison moderne","Création de jardins","Massifs, pelouse et cheminements dessinés pour votre terrain.")}
      {carte("plantation.jpg",1400,764,"Jardinier qui plante des vivaces dans un massif","Plantations","Arbustes, vivaces et haies plantés au bon endroit.")}
      {carte("taille-arbustes.jpg",1408,768,"Jardinier qui taille une haie au taille-haie devant une maison","Taille et haies","Haies et arbustes taillés proprement, coupes ramassées.")}
      {carte("entretien-general.jpg",1376,768,"Jardinier qui tond une pelouse devant une maison en pierre","Entretien du jardin","Tonte, désherbage et remise en ordre tout au long de l'année.")}
    </div></div></section>
  <section class="band craie" id="saisons"><div class="w">
    <div class="head"><span class="eyebrow">Au fil des saisons</span><h2>Chaque saison a ses gestes</h2><p>Quelques repères simples pour un jardin en bonne santé, de la tonte du printemps aux plantations d'automne.</p></div>
    <div class="saisons">{"".join(f'<div class="saison {c} rv"><span class="pastille">{IC[k]}</span><h3>{n}</h3><p>{l[0]}</p></div>' for k,n,c,l in SAISONS)}</div>
    <div class="cta" style="margin-top:36px"><a class="btn sapinbtn" href="conseils.html">Lire les conseils du jardinier</a></div>
  </div></section>
  <section class="band sapin" id="approche"><div class="w approche">
    <div class="photo"><img loading="lazy" src="images/conception.jpg" width="1408" height="768" alt="Plan de jardin affiché sur une tablette, discuté autour d'une table de jardin"></div>
    <div><span class="eyebrow">Notre approche</span><h2 style="margin-top:12px">Un jardin pensé avec vous</h2>
      <ol class="points">
        <li><span class="num">1</span><div><strong>Vous nous expliquez</strong><p>Votre terrain, vos habitudes, ce que vous attendez de votre extérieur.</p></div></li>
        <li><span class="num">2</span><div><strong>Nous proposons</strong><p>Un projet clair, discuté avec vous avant le début des travaux.</p></div></li>
        <li><span class="num">3</span><div><strong>Nous réalisons et suivons</strong><p>Les travaux, puis l'entretien si vous souhaitez garder la main légère.</p></div></li>
      </ol></div></div></section>
  <section class="contact"><div class="w box">
    <div><span class="eyebrow">Contact</span><h2 style="margin-top:12px">Parlons de votre jardin</h2><p>Appelez-nous pour décrire votre projet ou prendre rendez-vous. Nous vous répondons et fixons ensemble la suite.</p>
      <div class="cta"><a class="btn" href="contact.html">Écrire votre demande</a></div></div>
    {COORD}</div></section>'''
page("index.html","Ancelet Paysage | Paysagiste à Longnes (78)","Ancelet Paysage, paysagiste à Longnes dans les Yvelines : création de jardins, plantations, taille de haies et entretien.","index.html",home)

prest=f'''  <section class="ph"><div class="w">
    <div><span class="eyebrow">Prestations</span><h1>Deux façons de prendre soin de votre jardin</h1>
      <p>Créer un jardin ou un massif, ou garder le vôtre net toute l'année : choisissez par où commencer.</p>
      <div class="cta"><a class="btn" href="#creer">Créer</a><a class="btn ghost" href="#entretenir">Entretenir</a></div></div>
    <div class="mosaic">
      <img src="images/desherbage.jpg" width="1400" height="764" alt="Jardinier agenouillé qui désherbe un massif près d'un gravier">
      <img src="images/feuilles.jpg" width="1400" height="764" alt="Jardinier qui ratisse des feuilles mortes autour d'un massif">
      <img src="images/nettoyage.jpg" width="1376" height="768" alt="Jardinier qui évacue des tailles de végétaux avec une brouette">
    </div></div></section>
  <section class="band menthe" id="creer"><div class="w detail">
    <div><span class="eyebrow">Créer</span><h2 style="margin-top:12px">Un jardin dessiné pour votre terrain</h2>
      <ul class="liste">
        <li><strong>Création de jardins.</strong> Massifs, pelouse et cheminements, pensés selon votre terrain et vos usages.</li>
        <li><strong>Plantations.</strong> Arbustes, vivaces et haies, choisis et plantés au bon endroit.</li>
      </ul></div>
    <div class="photo"><img loading="lazy" src="images/allee-paves.jpg" width="1408" height="768" alt="Allée en pavés bordée d'un muret de pierre et de massifs"></div></div></section>
  <section class="band sapin" id="entretenir"><div class="w detail rev">
    <div><span class="eyebrow">Entretenir</span><h2 style="margin-top:12px">Un jardin net, toute l'année</h2>
      <ul class="liste">
        <li><strong>Tonte et désherbage.</strong> Pelouse et massifs remis en ordre.</li>
        <li><strong>Taille de haies et d'arbustes.</strong> Taille propre, coupes ramassées.</li>
        <li><strong>Évacuation des déchets verts.</strong> Branches et tontes chargées et emportées.</li>
      </ul></div>
    <div class="photo"><img loading="lazy" src="images/dechets-verts.jpg" width="1408" height="768" alt="Jardinier chargeant des branches et des déchets verts sur une remorque"></div></div></section>
  <section class="contact"><div class="w box">
    <div><span class="eyebrow">Un projet précis ?</span><h2 style="margin-top:12px">Décrivez-nous votre jardin</h2><p>Surface, plantations souhaitées, état actuel : quelques lignes suffisent pour lancer la discussion.</p>
      <div class="cta"><a class="btn" href="contact.html">Demander un devis</a></div></div>
    <div class="arche" style="max-width:380px;justify-self:center"><img loading="lazy" src="images/tonte.jpg" width="1376" height="768" alt="Jardinier qui tond une pelouse près d'une maison aux volets bleus" style="object-position:62% 50%"></div></div></section>'''
page("prestations.html","Prestations | Ancelet Paysage, Longnes","Création de jardins, plantations, taille de haies, tonte et évacuation des déchets verts : les prestations d'Ancelet Paysage à Longnes (78).","prestations.html",prest)

cons=f'''  <section class="ph"><div class="w">
    <div><span class="eyebrow">Conseils du jardinier</span><h1>Un jardin en forme, saison après saison</h1>
      <p>Des repères généraux pour entretenir votre jardin tout au long de l'année. Chaque terrain est différent : pour un avis sur le vôtre, parlons-en.</p>
      <div class="cta"><a class="btn" href="#saisons">Voir les saisons</a><a class="btn ghost" href="contact.html">Nous contacter</a></div></div>
    <div class="arche" style="max-width:380px;justify-self:center"><img src="images/feuilles.jpg" width="1400" height="764" alt="Jardinier qui ratisse des feuilles mortes autour d'un massif" style="object-position:35% 50%"></div></div></section>
  <section class="band craie" id="saisons"><div class="w">
    <div class="head"><span class="eyebrow">Les quatre saisons</span><h2>Que faire, et quand</h2><p>Des conseils généraux, à adapter selon votre sol, votre exposition et vos plantations.</p></div>
    <div class="saisons grand">{"".join(f'<article class="saison {c} rv"><span class="pastille">{IC[k]}</span><h3>{n}</h3><ul class="liste">'+"".join(f"<li>{t}</li>" for t in l)+'</ul></article>' for k,n,c,l in SAISONS)}</div>
  </div></section>
  <section class="band sapin"><div class="w detail">
    <div><span class="eyebrow">Toute l'année</span><h2 style="margin-top:12px">Trois habitudes qui font la différence</h2>
      <ul class="liste">
        <li><strong>Observer.</strong> Un coup d'œil régulier au jardin permet d'agir avant que les problèmes s'installent.</li>
        <li><strong>Pailler.</strong> Un sol couvert garde l'humidité et limite les herbes indésirables.</li>
        <li><strong>Garder les outils propres et affûtés.</strong> Une coupe nette cicatrise mieux sur les arbustes et les haies.</li>
      </ul></div>
    <div class="photo"><img loading="lazy" src="images/plantation.jpg" width="1400" height="764" alt="Jardinier qui plante des vivaces dans un massif"></div></div></section>
  <section class="contact"><div class="w box">
    <div><span class="eyebrow">Une question sur votre jardin ?</span><h2 style="margin-top:12px">Demandez conseil</h2><p>Décrivez votre terrain et ce qui vous pose problème : nous en discutons ensemble.</p>
      <div class="cta"><a class="btn" href="contact.html">Poser ma question</a></div></div>
    {COORD}</div></section>'''
page("conseils.html","Conseils du jardinier | Ancelet Paysage, Longnes","Conseils généraux d'entretien du jardin par saison : tonte, plantations, taille, arrosage et paillage, par Ancelet Paysage à Longnes (78).","conseils.html",cons)

cont=f'''  <section class="ph"><div class="w">
    <div><span class="eyebrow">Contact</span><h1>Un projet de jardin à Longnes ?</h1>
      <p>Appelez-nous, ou remplissez le formulaire : vous obtenez un message prêt à envoyer par SMS.</p>
      <a class="bigtel" href="tel:{TELL}">{TEL}</a></div>
    <div class="arche" style="max-width:380px;justify-self:center"><img src="images/taille-haies.jpg" width="1200" height="896" alt="Jardinier équipé d'un casque anti-bruit qui taille une haie" style="object-position:40% 50%"></div></div></section>
  <section class="band court menthe"><div class="w formgrid">
    <div><h2 style="margin-bottom:24px">Décrivez votre demande</h2>
      <form id="form" class="fcard" novalidate>
        <p class="fintro">Tous les champs sont obligatoires.</p>
        <div class="row">
          <label for="nom">Nom et prénom<input id="nom" name="nom" autocomplete="name" required aria-describedby="e-nom"><span class="err" id="e-nom" role="alert"></span></label>
          <label for="tel">Téléphone<input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="e-tel"><span class="err" id="e-tel" role="alert"></span></label>
        </div>
        <div class="row">
          <label for="commune">Commune du jardin<input id="commune" name="commune" autocomplete="address-level2" required aria-describedby="e-commune"><span class="err" id="e-commune" role="alert"></span></label>
          <label for="type">Type de travaux<select id="type" name="type" required aria-describedby="e-type"><option value="">Choisir…</option><option>Création de jardin</option><option>Plantations</option><option>Taille de haies et d'arbustes</option><option>Entretien (tonte, désherbage)</option><option>Autre</option></select><span class="err" id="e-type" role="alert"></span></label>
        </div>
        <label for="msg">Votre projet<textarea id="msg" name="msg" required aria-describedby="e-msg"></textarea><span class="err" id="e-msg" role="alert"></span></label>
        <button class="btn big" type="submit">Préparer ma demande</button>
      </form></div>
    <div>
      <div class="recap" id="recap" hidden aria-live="polite">
        <h3>Votre demande est prête</h3>
        <pre id="recap-txt"></pre>
        <div class="actions">
          <a class="btn" id="b-sms" href="#">Envoyer par SMS</a>
          <button class="btn ghost" type="button" id="b-copy">Copier</button>
          <a class="btn ghost" href="tel:{TELL}">Appeler</a>
        </div>
        <div class="ok" id="ok" role="status"></div>
      </div>
      <div id="avant" class="head" style="margin:0 0 24px"><span class="eyebrow">Comment ça marche</span><p>Ce site est une maquette : le formulaire ne s'envoie pas tout seul. Une fois rempli, il prépare votre message, que vous envoyez d'un clic par SMS ou que vous copiez.</p></div>
      {COORD}
    </div></div></section>'''
page("contact.html","Contact | Ancelet Paysage, Longnes","Contactez Ancelet Paysage à Longnes (78) pour un projet de jardin : téléphone, adresse et formulaire de demande de devis.","contact.html",cont)

leg=f'''  <section class="band court" style="padding-top:64px"><div class="w legal">
    <span class="eyebrow">Informations légales</span><h1 style="margin-top:12px">Mentions légales</h1>
    <h2>Éditeur du site</h2>
    <p>ANCELET PAYSAGE<br>SIREN : 433403052<br>Adresse : 4 B, 4 rue de Bréval, 78980 Longnes<br>Téléphone : {TEL}<br>Dirigeant au registre : Didier Louis Ancelet</p>
    <h2>Hébergement de la maquette</h2>
    <p>GitHub Pages (GitHub, Inc.).</p>
    <h2>Informations à compléter</h2>
    <p class="manque">Forme juridique, capital social, numéro de TVA, adresse e-mail, directeur de la publication et hébergeur définitif du futur site : non vérifiés à ce jour, à fournir par l'entreprise.</p>
    <h2>Maquette</h2>
    <p>Ce site est une maquette de démonstration présentée à l'entreprise. Les images sont illustratives et ne représentent pas des réalisations d'Ancelet Paysage.</p>
  </div></section>'''
page("mentions-legales.html","Mentions légales | Ancelet Paysage","Mentions légales du site d'Ancelet Paysage, paysagiste à Longnes (78).","",leg)
print("ok")

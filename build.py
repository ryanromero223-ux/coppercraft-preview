#!/usr/bin/env python3
"""Generate the three Coppercraft landing pages from content.py.

Usage: python3 build.py
Outputs 9-year.html, rye.html, blend.html next to this file.
Fonts are embedded (base64 woff2) so pages render identically offline,
deployed, and inside claude.ai Artifact previews (which block external hosts).
"""
import html as html_mod
from pathlib import Path

from content import (PAGES, STEPS, VARIANTS, STORE, STOREFRONT_TOKEN,
                     PIXEL_ID, SHIP_NOTE, FLAVIAR_LINE, PAYMENTS, PRESS)

PRESS_LOGOS = [
    ("USA Today", "assets/press/usa-today.png", 20),
    ("Whisky Advocate", "assets/press/whisky-advocate.svg", 24),
    ("The Whiskey Wash", "assets/press/whiskey-wash.png", 36),
    ("The Manual", "assets/press/the-manual.svg", 20),
    ("The Knockturnal", "assets/press/knockturnal.png", 17),
]
PRIVACY_URL = "https://coppercraftdistillery.com/terms-privacy/"
BASE_URL = "https://coppercraftwhiskey.com"
# Paste the code from Business Manager -> Brand safety -> Domains -> coppercraftwhiskey.com
META_DOMAIN_VERIFICATION = "u1y8xm7dxpoiahbb1w0u876bwdvzy1"

STEP_ICONS = [
    # bottle
    '<svg viewBox="0 0 24 24"><path d="M10 2h4M10.5 2v3.2c0 1.6-3 2.4-3 5V20a2 2 0 0 0 2 2h5a2 2 0 0 0 2-2V10.2c0-2.6-3-3.4-3-5V2"/><path d="M7.5 14h9"/></svg>',
    # shipping box
    '<svg viewBox="0 0 24 24"><path d="M3 8l9-5 9 5v8l-9 5-9-5z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v9"/><path d="M7.5 5.5l9 5"/></svg>',
    # signature pen
    '<svg viewBox="0 0 24 24"><path d="M3 21c3-1 4-1 6-3L20 7a2.2 2.2 0 0 0-3-3L6 15c-2 2-2 3-3 6z"/><path d="M13.5 6.5l3 3"/><path d="M13 21h8"/></svg>',
]

HERE = Path(__file__).parent
FONT_DIR = HERE / "fonts"

def font_b64(name):
    return (FONT_DIR / f"{name}.b64").read_text().strip()

def esc(s):
    return html_mod.escape(s, quote=False)

CSS_TEMPLATE = """
@font-face{font-family:'Oswald';font-style:normal;font-weight:500;src:url(data:font/woff2;base64,OSW500) format('woff2')}
@font-face{font-family:'Oswald';font-style:normal;font-weight:600;src:url(data:font/woff2;base64,OSW600) format('woff2')}
@font-face{font-family:'PT Serif';font-style:italic;font-weight:400;src:url(data:font/woff2;base64,PTSER) format('woff2')}
:root{
  --paper:#F2EDE3; --cream:#F0E6D2; --copper:ACCENT; --copper-dk:#96591F;
  --charcoal:#241F1A; --nearblack:#171310; --ink:#2b241d; --line:#DCD2BE;
  --disp:'Oswald','Arial Narrow',Arial,sans-serif;
  --body:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --serif:'PT Serif',Georgia,serif;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:var(--body);color:var(--ink);background:var(--paper);line-height:1.6;font-size:16px}
img{max-width:100%;display:block}
a{color:var(--copper-dk)}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
h1,h2,h3,.disp{font-family:var(--disp);font-weight:600;text-transform:uppercase;line-height:1.12;color:var(--charcoal);letter-spacing:.5px}
.eyebrow{font-family:var(--disp);font-weight:500;font-size:12px;letter-spacing:2.5px;color:var(--copper-dk);text-transform:uppercase;margin-bottom:14px}
.btn{display:block;width:100%;text-align:center;background:var(--copper);color:#fff;border:0;cursor:pointer;
     font-family:var(--disp);font-weight:600;font-size:19px;letter-spacing:1.5px;text-transform:uppercase;
     padding:17px 28px;border-radius:6px;text-decoration:none;transition:background .15s}
.btn:hover{background:var(--copper-dk)}
.btn[disabled]{opacity:.6;cursor:wait}
/* header */
.hdr{position:sticky;top:0;z-index:50;background:var(--nearblack);box-shadow:0 1px 0 rgba(255,255,255,.08)}
.hdr .wrap{display:flex;align-items:center;justify-content:space-between;padding-top:10px;padding-bottom:10px}
.hdr img{height:44px;width:auto}
.hdr a.hbtn{background:var(--copper);color:#fff;text-decoration:none;font-family:var(--disp);font-weight:600;
  font-size:13px;letter-spacing:1.2px;text-transform:uppercase;padding:9px 16px;border-radius:5px;white-space:nowrap}
/* hero */
.hero{padding:34px 0 50px}
.hero-grid{display:grid;grid-template-columns:1fr;gap:30px}
.hero-grid>*,.two>*{min-width:0}
@media(min-width:900px){.hero-grid{grid-template-columns:1.05fr .95fr;gap:44px;align-items:start}}
h1{font-size:clamp(27px,4.8vw,38px);margin:0 0 10px}
.tagline{font-family:var(--disp);font-weight:500;font-size:clamp(17px,2.6vw,21px);letter-spacing:.8px;text-transform:uppercase;color:var(--copper-dk);margin:0 0 12px;line-height:1.3}
.sub{font-size:17px;color:#4a4034;margin-bottom:18px}
.checks{list-style:none;margin:0 0 20px}
.checks li{padding-left:30px;position:relative;margin-bottom:9px;font-size:15.5px}
.checks li::before{content:"✓";position:absolute;left:0;top:0;color:var(--copper-dk);font-weight:700;font-size:17px}
/* carousel */
.car{position:relative}
.car-track{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;gap:0;border-radius:10px;scrollbar-width:none}
.car-track::-webkit-scrollbar{display:none}
.car-track img{flex:0 0 100%;aspect-ratio:1/1;object-fit:cover;scroll-snap-align:center;border-radius:10px}
.car-dots{display:flex;gap:8px;justify-content:center;margin-top:12px}
.car-dots button{width:9px;height:9px;border-radius:50%;border:0;background:#C9BCA0;cursor:pointer;padding:0}
.car-dots button.on{background:var(--copper-dk)}
.car-thumbs{display:flex;gap:8px;margin-top:12px;justify-content:center}
.car-thumbs img{width:56px;height:56px;object-fit:cover;border-radius:6px;cursor:pointer;border:2px solid transparent;opacity:.75}
.car-thumbs img.on{border-color:var(--copper);opacity:1}
/* buy box */
.tiers{display:flex;flex-direction:column;gap:10px;margin:6px 0 16px}
.tier{position:relative;display:flex;align-items:center;gap:13px;border:2px solid var(--line);border-radius:9px;
  padding:13px 15px;cursor:pointer;background:#fff;transition:border-color .12s}
.tier.on{border-color:var(--copper);background:#FCF8F0;box-shadow:0 0 0 1px var(--copper)}
.tier input{accent-color:var(--copper-dk);width:19px;height:19px;flex:none}
.tier .t-img{height:70px;width:auto;max-width:92px;object-fit:contain;flex:none}
.tier .t-main{flex:1;min-width:0}
.tier .t-label{font-family:var(--disp);font-weight:600;font-size:15px;letter-spacing:.8px;text-transform:uppercase;color:var(--charcoal)}
.tier .t-name{font-size:13px;color:#6b5d4a}
.tier .t-why{font-size:12.5px;color:#8a7a62;margin-top:2px}
.tier .t-price{font-family:var(--disp);font-weight:600;font-size:19px;color:var(--charcoal);white-space:nowrap}
.pop-badge{position:absolute;top:-10px;right:12px;background:var(--copper);color:#fff;font-family:var(--disp);
  font-weight:600;font-size:10.5px;letter-spacing:1.4px;padding:3px 10px;border-radius:20px;text-transform:uppercase}
.price-row{display:flex;align-items:baseline;gap:12px;margin:2px 0 4px}
.price-row .p{font-family:var(--disp);font-weight:600;font-size:34px;color:var(--charcoal)}
.price-row .s{font-size:13px;color:#8a7a62;letter-spacing:.4px}
.pay{display:flex;flex-wrap:wrap;gap:7px;margin:14px 0 10px}
.pay span{width:62px;height:34px;display:flex;align-items:center;justify-content:center;border:1px solid var(--line);border-radius:5px;background:#fff}
.pay img{max-height:19px;max-width:46px;width:auto;height:auto}
.trust{font-size:12px;color:#8a7a62;line-height:1.5}
.ship-note{font-size:12px;color:#8a7a62;margin-top:6px}
/* press */
.press{background:var(--nearblack);padding:22px 0}
.press .wrap{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:14px 34px}
.press .lbl{font-size:11px;letter-spacing:2.5px;color:#9b8a6f;font-family:var(--disp);font-weight:500}
.press img{filter:brightness(0) invert(.93) sepia(.2);opacity:.85;width:auto}
/* sections */
section.pad{padding:58px 0}
section.dark{background:var(--charcoal)}
section.dark h2,section.dark h3{color:var(--cream)}
section.dark p{color:#D9CDB6}
h2{font-size:clamp(24px,4vw,33px);margin-bottom:16px}
.two{display:grid;grid-template-columns:1fr;gap:28px;align-items:center}
@media(min-width:840px){.two{grid-template-columns:1fr 1fr;gap:48px}}
.two img{border-radius:10px;width:100%;object-fit:cover;max-height:460px}
.two p{margin-bottom:13px;font-size:16px}
.cards{display:grid;grid-template-columns:1fr;gap:14px;margin-top:26px}
@media(min-width:760px){.cards{grid-template-columns:repeat(3,1fr)}}
.card{background:var(--nearblack);border:1px solid #3a322a;border-radius:10px;padding:22px 20px}
.card h3{font-size:20px;color:var(--copper);letter-spacing:1.2px;margin-bottom:8px}
.card p{font-size:14.5px;color:#D9CDB6;margin:0}
/* quotes */
.quotes{display:grid;grid-template-columns:1fr;gap:18px}
@media(min-width:840px){.quotes{grid-template-columns:repeat(QCOLS,1fr)}}
.q{background:#fff;border:1px solid var(--line);border-radius:10px;padding:26px 24px}
.q p{font-family:var(--serif);font-style:italic;font-size:18.5px;line-height:1.5;color:var(--charcoal);margin-bottom:12px}
.q .who{font-family:var(--disp);font-weight:500;font-size:11.5px;letter-spacing:1.8px;text-transform:uppercase;color:var(--copper-dk)}
/* compare */
table.cmp{width:100%;border-collapse:collapse;background:#fff;border-radius:10px;overflow:hidden;border:1px solid var(--line)}
.cmp th,.cmp td{padding:13px 14px;text-align:left;font-size:14.5px;border-bottom:1px solid var(--line)}
.cmp thead th{font-family:var(--disp);font-weight:600;letter-spacing:1px;text-transform:uppercase;font-size:13px}
.cmp thead th:nth-child(2){color:#8a7a62}
.cmp thead th:nth-child(3){background:var(--charcoal);color:var(--cream)}
.cmp td:first-child{font-weight:600;color:var(--charcoal);width:26%}
.cmp td:nth-child(2){color:#8a7a62}
.cmp td:nth-child(3){background:#FCF8F0;color:var(--charcoal);font-weight:600}
.cmp tr:last-child td{border-bottom:0}
.cmp-wrap{overflow-x:auto}
.cmp-note{margin-top:16px;font-size:15px}
.cmp-note .qq{font-family:var(--serif);font-style:italic;font-size:17px;color:var(--charcoal)}
/* steps */
.steps{display:grid;grid-template-columns:1fr;gap:16px;margin-top:26px}
@media(min-width:760px){.steps{grid-template-columns:repeat(3,1fr)}}
.step{background:#fff;border:1px solid var(--line);border-radius:10px;padding:22px}
.step .n{color:#fff;background:var(--copper);width:40px;height:40px;
  border-radius:50%;display:flex;align-items:center;justify-content:center;margin-bottom:12px}
.step .n svg{width:20px;height:20px;stroke:#fff;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.step h3{font-size:17px;letter-spacing:1px;margin-bottom:7px}
.step p{font-size:14px;color:#5d5245;margin:0}
/* faq */
.faq details{background:#fff;border:1px solid var(--line);border-radius:9px;margin-bottom:10px;overflow:hidden}
.faq summary{cursor:pointer;padding:16px 44px 16px 18px;font-weight:600;color:var(--charcoal);font-size:15.5px;list-style:none;position:relative}
.faq summary::-webkit-details-marker{display:none}
.faq summary::after{content:"+";position:absolute;right:18px;top:50%;transform:translateY(-50%);font-size:22px;color:var(--copper-dk);font-weight:400}
.faq details[open] summary::after{content:"–"}
.faq .a{padding:0 18px 16px;font-size:15px;color:#5d5245}
/* final */
.final{background:var(--nearblack);text-align:center}
.final h2{color:var(--cream)}
.final p{color:#C9BCA0;margin-bottom:22px}
.final .btn{max-width:420px;margin:0 auto}
.final img{height:230px;width:auto;margin:0 auto 20px}
/* footer */
footer{background:var(--nearblack);border-top:1px solid #35291d;padding:38px 0 90px;color:#9b8a6f;font-size:12.5px}
footer .wrap{display:flex;flex-direction:column;gap:14px;align-items:center;text-align:center}
footer img{height:56px;width:auto;opacity:.9}
footer .resp{font-family:var(--disp);font-weight:600;letter-spacing:2.5px;color:var(--cream);font-size:13px}
footer nav{display:flex;gap:22px}
footer nav a{color:#C9BCA0;text-decoration:none;font-size:13px}
/* sticky mobile bar */
.mbar{position:fixed;left:0;right:0;bottom:0;z-index:60;background:var(--nearblack);padding:10px 14px;
  display:flex;align-items:center;gap:12px;transform:translateY(110%);transition:transform .25s;box-shadow:0 -4px 16px rgba(0,0,0,.3)}
.mbar.show{transform:translateY(0)}
.mbar .mp{font-family:var(--disp);font-weight:600;color:var(--cream);font-size:18px;white-space:nowrap}
.mbar .btn{padding:12px 16px;font-size:15px}
@media(min-width:900px){.mbar{display:none} footer{padding-bottom:38px}}
/* cart drawer */
.cart-ov{position:fixed;inset:0;background:rgba(16,12,8,.55);z-index:80;opacity:0;pointer-events:none;transition:opacity .2s}
.cart-ov.open{opacity:1;pointer-events:auto}
.drawer{position:fixed;top:0;right:0;bottom:0;width:min(420px,100%);background:var(--paper);z-index:90;transform:translateX(105%);transition:transform .25s;display:flex;flex-direction:column;box-shadow:-8px 0 30px rgba(0,0,0,.25)}
.drawer.open{transform:none}
.d-head{display:flex;align-items:center;justify-content:space-between;padding:15px 18px;background:var(--nearblack)}
.d-head .t{font-family:var(--disp);font-weight:600;font-size:18px;letter-spacing:1.2px;text-transform:uppercase;color:var(--cream)}
.d-head button{background:none;border:0;color:var(--cream);font-size:24px;cursor:pointer;line-height:1;padding:2px 6px}
.d-timer{background:var(--cream);color:var(--charcoal);text-align:center;font-size:13.5px;padding:9px 12px;border-bottom:1px solid var(--line)}
.d-timer b{font-variant-numeric:tabular-nums}
.d-items{flex:1;overflow-y:auto;padding:6px 18px}
.d-row{display:flex;gap:13px;align-items:center;padding:14px 0;border-bottom:1px solid var(--line)}
.d-row img{height:66px;width:auto}
.d-row .m{flex:1;min-width:0}
.d-row .nm{font-weight:600;color:var(--charcoal);font-size:14.5px}
.d-row .pr{font-family:var(--disp);font-weight:600;color:var(--charcoal);font-size:15px;margin-top:2px}
.qty{display:inline-flex;border:1px solid var(--line);border-radius:6px;overflow:hidden;margin-top:8px;background:#fff}
.qty button{width:29px;height:27px;border:0;background:#fff;cursor:pointer;font-size:15px;color:var(--charcoal)}
.qty span{width:30px;text-align:center;font-size:13.5px;line-height:27px}
.d-row .rm{background:none;border:0;cursor:pointer;color:#8a7a62;padding:4px}
.d-row .rm svg{width:17px;height:17px;stroke:currentColor;fill:none;stroke-width:1.8}
.d-empty{text-align:center;color:#8a7a62;padding:26px 20px 10px;font-size:14.5px}
.d-foot{padding:14px 18px 18px;border-top:1px solid var(--line)}
.d-foot .pay{justify-content:center;margin:12px 0 0}
/* lineup progress */
.d-progress{padding:12px 18px 10px;border-bottom:1px solid var(--line)}
.d-progress .dp-t{font-family:var(--disp);font-weight:500;font-size:12px;letter-spacing:1.4px;text-transform:uppercase;color:#6b5d4a;text-align:center;margin-bottom:8px}
.dp-bar{display:flex;gap:5px}
.dp-bar i{flex:1;height:5px;border-radius:3px;background:var(--line)}
.dp-bar i.on{background:var(--copper)}
/* complete-the-lineup cross-sell */
.dx-h{font-family:var(--disp);font-weight:600;font-size:13px;letter-spacing:1.4px;text-transform:uppercase;color:var(--charcoal);padding:16px 0 2px}
.dx-row{display:flex;gap:13px;align-items:center;padding:12px 0;border-bottom:1px solid var(--line)}
.dx-row img{height:54px;width:auto}
.dx-row .m{flex:1;min-width:0}
.dx-row .nm{font-weight:600;color:var(--charcoal);font-size:13.5px}
.dx-row .pr{font-size:13px;color:#6b5d4a;margin-top:1px}
.dx-add{background:var(--copper);color:#fff;border:0;border-radius:6px;padding:9px 14px;cursor:pointer;font-family:var(--disp);font-weight:600;font-size:13px;letter-spacing:.8px;text-transform:uppercase;white-space:nowrap}
.dx-add:hover{background:var(--copper-dk)}
/* drawer press strip */
.d-press{margin-top:12px;text-align:center}
.d-press .lb{font-family:var(--disp);font-size:10.5px;letter-spacing:1.8px;text-transform:uppercase;color:#8a7a62;margin-bottom:7px}
.d-press .row{display:flex;justify-content:center;align-items:center;gap:13px;flex-wrap:wrap}
.d-press img{filter:brightness(0);opacity:.5;width:auto}
.hdr-right{display:flex;align-items:center;gap:12px}
.cartbtn{position:relative;background:none;border:0;cursor:pointer;padding:4px}
.cartbtn svg{width:25px;height:25px;stroke:var(--cream);fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.cartbtn .ct{position:absolute;top:-5px;right:-7px;background:var(--copper);color:#fff;font-size:10.5px;font-weight:700;border-radius:10px;min-width:17px;height:17px;line-height:17px;text-align:center;padding:0 3px;display:none}
.btn svg.bic{width:19px;height:19px;stroke:#fff;fill:none;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round;vertical-align:-3px;margin-right:9px}
/* age gate */
#age{position:fixed;inset:0;z-index:100;background:rgba(16,12,8,.94);display:flex;align-items:center;justify-content:center;padding:20px}
#age .box{background:var(--paper);border-radius:12px;max-width:420px;width:100%;padding:38px 30px;text-align:center}
#age img{height:64px;margin:0 auto 18px;filter:invert(.85) sepia(.3)}
#age h2{font-size:24px;margin-bottom:8px}
#age p{font-size:14px;color:#5d5245;margin-bottom:22px}
#age .row{display:flex;gap:10px}
#age button{flex:1;padding:13px;border-radius:6px;border:0;cursor:pointer;font-family:var(--disp);font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase}
#age .yes{background:var(--copper);color:#fff}
#age .no{background:#DCD2BE;color:var(--charcoal)}
body.gated{overflow:hidden}
"""

JS_TEMPLATE = r"""
(function(){
  var CARTSVG='<svg class="bic" viewBox="0 0 24 24"><path d="M6 7h12l1.2 12.2a1.8 1.8 0 0 1-1.8 1.8H6.6a1.8 1.8 0 0 1-1.8-1.8L6 7z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg>';
  /* ---------- age gate ---------- */
  var gate=document.getElementById('age');
  try{ if(localStorage.getItem('cc21')==='1'){gate.remove();} else {document.body.classList.add('gated');} }catch(e){document.body.classList.add('gated');}
  window.ageYes=function(){try{localStorage.setItem('cc21','1');}catch(e){} gate.remove(); document.body.classList.remove('gated');};
  window.ageNo=function(){window.location.href='https://www.responsibility.org/';};

  /* ---------- carousel ---------- */
  var track=document.querySelector('.car-track');
  var dots=[].slice.call(document.querySelectorAll('.car-dots button'));
  var thumbs=[].slice.call(document.querySelectorAll('.car-thumbs img'));
  function setOn(i){
    dots.forEach(function(d,j){d.classList.toggle('on',j===i);});
    thumbs.forEach(function(t,j){t.classList.toggle('on',j===i);});
  }
  function go(i){ track.scrollTo({left:track.clientWidth*i,behavior:'smooth'}); }
  dots.forEach(function(d,i){d.addEventListener('click',function(){go(i);});});
  thumbs.forEach(function(t,i){t.addEventListener('click',function(){go(i);});});
  track.addEventListener('scroll',function(){
    var i=Math.round(track.scrollLeft/track.clientWidth); setOn(i);
  },{passive:true});
  setOn(0);

  /* ---------- tiers ---------- */
  var VARIANTS=__VARIANTS__;
  var TIERS=__TIERS__;
  var PRICES={nine:37.99,rye:37.99,blend:42.95};
  var NAMES={nine:'9-Year Straight Bourbon',rye:'Rye Whiskey',blend:'Blend of Straight Bourbons'};
  var THUMBS={nine:'assets/cutout-9yr.png',rye:'assets/cutout-rye.png',blend:'assets/cutout-blend.png'};
  var picked=TIERS.findIndex(function(t){return t.popular;}); if(picked<0)picked=0;
  var tierEls=[].slice.call(document.querySelectorAll('.tier'));
  function pick(i){
    picked=i;
    tierEls.forEach(function(el,j){
      el.classList.toggle('on',j===i);
      el.querySelector('input').checked=(j===i);
    });
    [].slice.call(document.querySelectorAll('.cta-price')).forEach(function(s){s.textContent=TIERS[i].price;});
  }
  tierEls.forEach(function(el,i){el.addEventListener('click',function(){pick(i);});});
  pick(picked);

  /* ---------- cart (shared across the 3 pages via localStorage) ---------- */
  var RESERVE_MS=10*60*1000;
  function loadCart(){ try{ return JSON.parse(localStorage.getItem('ccCartV1'))||{items:{},exp:0}; }catch(e){ return {items:{},exp:0}; } }
  function saveCart(){ try{ localStorage.setItem('ccCartV1',JSON.stringify(cart)); }catch(e){} }
  var cart=loadCart();
  var drawer=document.querySelector('.drawer'), ov=document.querySelector('.cart-ov');
  function money(n){ return '$'+n.toFixed(2); }
  function count(){ var n=0; for(var k in cart.items) n+=cart.items[k]; return n; }
  function subtotal(){ var s=0; for(var k in cart.items) s+=PRICES[k]*cart.items[k]; return s; }
  function openCart(){ drawer.classList.add('open'); ov.classList.add('open'); }
  function closeCart(){ drawer.classList.remove('open'); ov.classList.remove('open'); }
  window.ccCloseCart=closeCart;
  ov.addEventListener('click',closeCart);

  function distinct(){ var n=0; for(var k in PRICES) if(cart.items[k]>0) n++; return n; }
  function addOne(k){
    cart.items[k]=(cart.items[k]||0)+1;
    cart.exp=Date.now()+RESERVE_MS;
    saveCart(); render(); tick();
    try{ if(window.fbq){ fbq('track','AddToCart',{content_type:'product',content_ids:[VARIANTS[k]],value:PRICES[k],currency:'USD'}); } }catch(e){}
  }
  function render(){
    var box=drawer.querySelector('.d-items');
    var keys=Object.keys(cart.items).filter(function(k){return cart.items[k]>0;});
    var badge=document.querySelector('.cartbtn .ct');
    var n=count();
    if(badge){ badge.textContent=n; badge.style.display=n?'block':'none'; }
    drawer.querySelector('.d-head .t').textContent='Cart · '+n;
    /* lineup progress bar */
    var d=distinct();
    drawer.querySelector('.d-progress .dp-t').textContent=(d===3)?'The full lineup is in your cart':d+' of 3 bottles in the lineup';
    [].slice.call(drawer.querySelectorAll('.dp-bar i')).forEach(function(seg,i){ seg.className=(i<d)?'on':''; });
    /* complete-the-lineup rows for whatever is missing */
    var missing=Object.keys(PRICES).filter(function(k){return !cart.items[k];});
    var cross='';
    if(missing.length){
      cross='<div class="dx-h">'+(keys.length?'Complete the lineup':'Pick your bottle')+'</div>'
        +missing.map(function(k){
          return '<div class="dx-row">'
            +'<img src="'+THUMBS[k]+'" alt="">'
            +'<div class="m"><div class="nm">Coppercraft '+NAMES[k]+'</div><div class="pr">'+money(PRICES[k])+'</div></div>'
            +'<button class="dx-add" data-k="'+k+'">+ Add</button></div>';
        }).join('');
    }
    if(!keys.length){
      box.innerHTML='<div class="d-empty">Your glass is ready when you are.</div>'+cross;
      drawer.querySelector('.d-co').style.display='none';
    }else{
      drawer.querySelector('.d-co').style.display='block';
      var trash='<svg viewBox="0 0 24 24"><path d="M4 7h16M9 7V5a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v2m3 0l-1 13a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2L6 7"/></svg>';
      box.innerHTML=keys.map(function(k){
        return '<div class="d-row" data-k="'+k+'">'
          +'<img src="'+THUMBS[k]+'" alt="">'
          +'<div class="m"><div class="nm">Coppercraft '+NAMES[k]+'</div><div class="pr">'+money(PRICES[k]*cart.items[k])+'</div>'
          +'<div class="qty"><button data-d="-1">−</button><span>'+cart.items[k]+'</span><button data-d="1">+</button></div></div>'
          +'<button class="rm" aria-label="Remove">'+trash+'</button></div>';
      }).join('')+cross;
      drawer.querySelector('.d-co .btn').innerHTML=CARTSVG+'Checkout · '+money(subtotal());
      [].slice.call(box.querySelectorAll('.qty button')).forEach(function(b){
        b.addEventListener('click',function(){
          var k=b.closest('.d-row').dataset.k;
          cart.items[k]=Math.max(0,(cart.items[k]||0)+parseInt(b.dataset.d,10));
          if(!cart.items[k]) delete cart.items[k];
          saveCart(); render();
        });
      });
      [].slice.call(box.querySelectorAll('.rm')).forEach(function(b){
        b.addEventListener('click',function(){
          delete cart.items[b.closest('.d-row').dataset.k];
          saveCart(); render();
        });
      });
    }
    [].slice.call(box.querySelectorAll('.dx-add')).forEach(function(b){
      b.addEventListener('click',function(){ addOne(b.dataset.k); });
    });
  }

  /* reservation timer */
  function tick(){
    var el=drawer.querySelector('.d-timer');
    var left=cart.exp-Date.now();
    if(count()&&left>0){
      var m=Math.floor(left/60000), s=Math.floor(left%60000/1000);
      el.style.display='block';
      el.innerHTML='Your bottles are reserved for <b>'+(m<10?'0':'')+m+':'+(s<10?'0':'')+s+'</b>';
    }else{ el.style.display='none'; }
  }
  setInterval(tick,1000);

  function addTier(){
    var t=TIERS[picked];
    t.items.forEach(function(x){ cart.items[x[0]]=(cart.items[x[0]]||0)+x[1]; });
    cart.exp=Date.now()+RESERVE_MS;
    saveCart(); render(); tick(); openCart();
    try{ if(window.fbq){ fbq('track','AddToCart',{content_type:'product',content_ids:t.items.map(function(x){return VARIANTS[x[0]];}),value:t.value,currency:'USD'}); } }catch(e){}
  }
  [].slice.call(document.querySelectorAll('.js-buy')).forEach(function(b){b.addEventListener('click',addTier);});
  var hdrCart=document.querySelector('.cartbtn');
  if(hdrCart) hdrCart.addEventListener('click',function(){ render(); tick(); openCart(); });

  /* checkout from the drawer */
  function checkoutCart(){
    var keys=Object.keys(cart.items).filter(function(k){return cart.items[k]>0;});
    if(!keys.length) return;
    var btn=drawer.querySelector('.d-co .btn');
    btn.setAttribute('disabled',''); btn.textContent='OPENING SECURE CHECKOUT…';
    try{ if(window.fbq){ fbq('track','InitiateCheckout',{value:subtotal(),currency:'USD'}); } }catch(e){}
    var lines=keys.map(function(k){return {merchandiseId:'gid://shopify/ProductVariant/'+VARIANTS[k],quantity:cart.items[k]};});
    var q='mutation($lines:[CartLineInput!]!){cartCreate(input:{lines:$lines}){cart{checkoutUrl}userErrors{message}}}';
    fetch('https://__STORE__/api/2024-01/graphql.json',{
      method:'POST',
      headers:{'Content-Type':'application/json','X-Shopify-Storefront-Access-Token':'__TOKEN__'},
      body:JSON.stringify({query:q,variables:{lines:lines}})
    }).then(function(r){return r.json();}).then(function(d){
      var url=d&&d.data&&d.data.cartCreate&&d.data.cartCreate.cart&&d.data.cartCreate.cart.checkoutUrl;
      if(url){ window.location.href=url; } else { fallback(keys); }
    }).catch(function(){ fallback(keys); });
    setTimeout(function(){ btn.removeAttribute('disabled'); render(); },9000);
  }
  function fallback(keys){
    if(keys.length===1 && keys[0]!=='rye'){
      window.location.href='https://__STORE__/cart/'+VARIANTS[keys[0]]+':'+cart.items[keys[0]];
    }else{
      window.location.href='https://coppercraftdistillery.com/buy-online/';
    }
  }
  drawer.querySelector('.d-co .btn').addEventListener('click',checkoutCart);
  render(); tick();

  /* ---------- mobile bar ---------- */
  var bar=document.querySelector('.mbar');
  var buybox=document.getElementById('buy');
  if('IntersectionObserver' in window && bar && buybox){
    new IntersectionObserver(function(en){
      bar.classList.toggle('show',!en[0].isIntersecting && en[0].boundingClientRect.top<0);
    },{threshold:0}).observe(buybox);
  }
})();
"""

PIXEL_TMPL = """
<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{pixel}');
fbq('track', 'PageView');
fbq('track', 'ViewContent', {{content_type:'product', content_name:'{name}', content_ids:['{vid}'], value:{value}, currency:'USD'}});
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id={pixel}&ev=PageView&noscript=1"/></noscript>
"""


def render(pagekey):
    p = PAGES[pagekey]
    css = (CSS_TEMPLATE
           .replace("OSW500", font_b64("Oswald-500-normal"))
           .replace("OSW600", font_b64("Oswald-600-normal"))
           .replace("PTSER", font_b64("PT Serif-400-italic"))
           .replace("ACCENT", p["accent"])
           .replace("QCOLS", str(min(3, len(p["quotes"])))))

    tiers_js = [{"key": t["key"], "price": t["price"],
                 "value": float(t["price"].replace("$", "")),
                 "items": t["items"], "popular": t["popular"]} for t in p["tiers"]]
    import json
    js = (JS_TEMPLATE
          .replace("__VARIANTS__", json.dumps(VARIANTS))
          .replace("__TIERS__", json.dumps(tiers_js))
          .replace("__STORE__", STORE)
          .replace("__TOKEN__", STOREFRONT_TOKEN))

    single_vid = VARIANTS[p["tiers"][0]["items"][0][0]]
    pixel = PIXEL_TMPL.format(pixel=PIXEL_ID, name=p["sku_name"],
                              vid=single_vid,
                              value=p["price"].replace("$", ""))

    # ---- fragments ----
    car_imgs = "\n".join(f'<img src="{s}" alt="{esc(a)}" loading="{"eager" if i==0 else "lazy"}">'
                         for i, (s, a) in enumerate(p["carousel"]))
    car_dots = "\n".join(f'<button aria-label="Photo {i+1}"></button>' for i in range(len(p["carousel"])))
    car_thumbs = "\n".join(f'<img src="{s}" alt="" loading="lazy">' for s, a in p["carousel"])

    bullets = "\n".join(f"<li>{esc(b)}</li>" for b in p["bullets"])

    cutmap = {"nine": "assets/cutout-9yr.png", "rye": "assets/cutout-rye.png", "blend": "assets/cutout-blend.png"}
    tier_cards = []
    for i, t in enumerate(p["tiers"]):
        badge = '<span class="pop-badge">Most Popular</span>' if t["popular"] else ""
        skus = [x[0] for x in t["items"]]
        if len(skus) == 1:
            img = cutmap[skus[0]]
        elif len(skus) == 2:
            img = f"assets/combo-{skus[0]}-{skus[1]}.png"
        else:
            img = f"assets/combo-trio-{skus[0]}.png"
        tier_cards.append(f"""
      <label class="tier">{badge}
        <input type="radio" name="tier" {'checked' if t['popular'] else ''}>
        <img class="t-img" src="{img}" alt="" loading="lazy">
        <span class="t-main">
          <span class="t-label">{esc(t['label'])}</span>
          <span class="t-name">{esc(t['name'])}</span>
          <span class="t-why">{esc(t['why'])}</span>
        </span>
        <span class="t-price">{t['price']}</span>
      </label>""")
    tiers_html = "\n".join(tier_cards)

    pay = "\n".join(f'<span><img src="{f}" alt="{esc(n)}" loading="lazy"></span>' for n, f in PAYMENTS)
    press = "\n".join(f'<img src="{f}" alt="{esc(n)}" style="height:{h}px" loading="lazy">'
                      for n, f, h in PRESS_LOGOS)
    # compact press strip for the cart drawer (same verified outlets, ~60% scale)
    drawer_press = "\n".join(f'<img src="{f}" alt="{esc(n)}" style="height:{max(11, int(h*0.62))}px" loading="lazy">'
                             for n, f, h in PRESS_LOGOS)

    problem_ps = "\n".join(f"<p>{esc(x)}</p>" for x in p["problem_ps"])
    mech_cards = "\n".join(f'<div class="card"><h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
                           for t, b in p["mech_cards"])
    quotes = "\n".join(
        f'<div class="q"><p>“{esc(q.strip(chr(34)))}”</p><div class="who">{esc(w)}</div></div>'
        for q, w in p["quotes"])

    rows = "\n".join(f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>"
                     for a, b, c in p["compare_rows"])
    cq = p.get("compare_quote")
    cmp_note = ((f'<p class="cmp-note"><span class="qq">“{esc(cq.strip(chr(34)))}”</span><br>{esc(p["compare_note"])}</p>')
                if cq else f'<p class="cmp-note">{esc(p["compare_note"])}</p>')

    gift_ps = "\n".join(f"<p>{esc(x)}</p>" for x in p["gift_ps"])
    steps = "\n".join(f'<div class="step"><div class="n">{STEP_ICONS[i]}</div><h3>{esc(t)}</h3><p>{esc(b)}</p></div>'
                      for i, (t, b) in enumerate(STEPS))
    faq = "\n".join(f'<details><summary>{esc(q)}</summary><div class="a">{esc(a)}</div></details>'
                    for q, a in p["faq"])
    cross = " · ".join(f'<a href="{h}">{esc(n)}</a>' for h, n in p["cross"])

    doc = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(p['title'])}</title>
<meta name="description" content="{esc(p['meta_desc'])}">
<meta name="robots" content="noindex">
<link rel="canonical" href="{BASE_URL}/{p['file'].replace('.html','')}/">
{f'<meta name="facebook-domain-verification" content="{META_DOMAIN_VERIFICATION}">' if META_DOMAIN_VERIFICATION else '<!-- facebook-domain-verification tag goes here once Ryan pulls the code from Business Manager -->'}
<style>{css}</style>
{pixel}
</head>
<body>

<div id="age">
  <div class="box">
    <img src="assets/logo-white.png" alt="Coppercraft Distillery">
    <h2>Are you 21 or older?</h2>
    <p>You must be of legal drinking age to enter this site.</p>
    <div class="row">
      <button class="yes" onclick="ageYes()">Yes, I'm 21+</button>
      <button class="no" onclick="ageNo()">No</button>
    </div>
  </div>
</div>

<header class="hdr">
  <div class="wrap">
    <img src="assets/logo-white.png" alt="Coppercraft Distillery, Holland, Michigan">
    <div class="hdr-right">
      <a class="hbtn" href="#buy">Get the bottle · {p['price']}</a>
      <button class="cartbtn" aria-label="Cart">
        <svg viewBox="0 0 24 24"><path d="M6 7h12l1.2 12.2a1.8 1.8 0 0 1-1.8 1.8H6.6a1.8 1.8 0 0 1-1.8-1.8L6 7z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg>
        <span class="ct"></span>
      </button>
    </div>
  </div>
</header>

<div class="cart-ov"></div>
<aside class="drawer" aria-label="Cart">
  <div class="d-head"><span class="t">Cart</span><button onclick="ccCloseCart()" aria-label="Close">×</button></div>
  <div class="d-timer" style="display:none"></div>
  <div class="d-progress"><div class="dp-t"></div><div class="dp-bar"><i></i><i></i><i></i></div></div>
  <div class="d-items"></div>
  <div class="d-foot d-co" style="display:none">
    <button class="btn">Checkout</button>
    <div class="d-press"><div class="lb">As featured in</div><div class="row">{drawer_press}</div></div>
    <div class="pay">{pay}</div>
  </div>
</aside>

<section class="hero">
  <div class="wrap hero-grid">
    <div class="car">
      <div class="car-track">{car_imgs}</div>
      <div class="car-dots">{car_dots}</div>
      <div class="car-thumbs">{car_thumbs}</div>
    </div>
    <div>
      <h1>{esc(p['h1'])}</h1>
      <p class="tagline">{esc(p['tagline'])}</p>
      <p class="sub">{esc(p['sub'])}</p>
      <ul class="checks">{bullets}</ul>
      <div id="buy">
        <div class="price-row"><span class="p">{p['price']}</span><span class="s">{esc(p['specs'])}</span></div>
        <div class="tiers">{tiers_html}</div>
        <button class="btn js-buy"><svg class="bic" viewBox="0 0 24 24"><path d="M6 7h12l1.2 12.2a1.8 1.8 0 0 1-1.8 1.8H6.6a1.8 1.8 0 0 1-1.8-1.8L6 7z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg>Add to Cart · <span class="cta-price">{p['price']}</span></button>
        <div class="pay">{pay}</div>
        <p class="trust">{esc(FLAVIAR_LINE)}</p>
        <p class="ship-note">{esc(SHIP_NOTE)}</p>
      </div>
    </div>
  </div>
</section>

<div class="press">
  <div class="wrap">
    <span class="lbl">FEATURED IN</span>
    {press}
  </div>
</div>

<section class="pad">
  <div class="wrap two">
    <div>
      <h2>{esc(p['problem_h2'])}</h2>
      {problem_ps}
    </div>
    <img src="{p['problem_img'][0]}" alt="{esc(p['problem_img'][1])}" loading="lazy">
  </div>
</section>

<section class="pad dark">
  <div class="wrap">
    <h2>{esc(p['mech_h2'])}</h2>
    <p>{esc(p['mech_intro'])}</p>
    <div class="cards">{mech_cards}</div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <div class="quotes">{quotes}</div>
  </div>
</section>

<section class="pad" style="padding-top:0">
  <div class="wrap">
    <h2>{esc(p['compare_h2'])}</h2>
    <div class="cmp-wrap">
    <table class="cmp">
      <thead><tr><th></th><th>{esc(p['compare_cols'][0])}</th><th>{esc(p['compare_cols'][1])}</th></tr></thead>
      <tbody>{rows}</tbody>
    </table>
    </div>
    {cmp_note}
  </div>
</section>

<section class="pad dark">
  <div class="wrap two">
    <img src="{p['gift_img'][0]}" alt="{esc(p['gift_img'][1])}" loading="lazy">
    <div>
      <h2>{esc(p['gift_h2'])}</h2>
      {gift_ps}
      <a class="btn" style="max-width:340px" href="#buy">See the bottle options</a>
    </div>
  </div>
</section>

<section class="pad">
  <div class="wrap">
    <h2>How ordering works</h2>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="pad" style="padding-top:0">
  <div class="wrap faq" style="max-width:760px">
    <h2>Questions, answered</h2>
    {faq}
  </div>
</section>

<section class="pad final">
  <div class="wrap">
    <img src="{cutmap[p['tiers'][0]['items'][0][0]]}" alt="{esc(p['sku_name'])}" loading="lazy">
    <h2>{esc(p['final_h2'])}</h2>
    <p>{esc(p['final_sub'])}</p>
    <a class="btn" href="#buy">Add to Cart · {p['price']}</a>
  </div>
</section>

<footer>
  <div class="wrap">
    <img src="assets/logo-white.png" alt="Coppercraft Distillery">
    <div class="resp">DRINK RESPONSIBLY · 21+</div>
    <nav>{cross} · <a href="{PRIVACY_URL}">Terms &amp; Privacy</a></nav>
    <div>{esc(FLAVIAR_LINE)}</div>
    <div>{esc(SHIP_NOTE)}</div>
    <div>© 2026 Coppercraft Distillery · Holland, Michigan · Est. 2012</div>
  </div>
</footer>

<div class="mbar">
  <span class="mp"><span class="cta-price">{p['price']}</span></span>
  <button class="btn js-buy"><svg class="bic" viewBox="0 0 24 24"><path d="M6 7h12l1.2 12.2a1.8 1.8 0 0 1-1.8 1.8H6.6a1.8 1.8 0 0 1-1.8-1.8L6 7z"/><path d="M9 9V6a3 3 0 0 1 6 0v3"/></svg>Add to Cart</button>
</div>

<script>{js}</script>
</body>
</html>"""
    return p["file"], doc


def render_hub():
    """Public-facing home for coppercraftwhiskey.com/ — the 3-bottle storefront."""
    fonts = "\n".join([
        "@font-face{font-family:'Oswald';font-style:normal;font-weight:500;src:url(data:font/woff2;base64,%s) format('woff2')}" % font_b64("Oswald-500-normal"),
        "@font-face{font-family:'Oswald';font-style:normal;font-weight:600;src:url(data:font/woff2;base64,%s) format('woff2')}" % font_b64("Oswald-600-normal"),
    ])
    cutmap = {"nine": "assets/cutout-9yr.png", "rye": "assets/cutout-rye.png", "blend": "assets/cutout-blend.png"}
    skumap = {"9-year.html": "nine", "rye.html": "rye", "blend.html": "blend"}
    cards = "\n".join(
        f'''<a class="card" href="{p['file'].replace('.html','')}/">
      <img src="{cutmap[skumap[p['file']]]}" alt="{esc(p['sku_name'])}" loading="lazy">
      <div class="ct">
        <div class="n">{esc(p['sku_name'])}</div>
        <div class="d">{esc(p['tagline'])}</div>
        <div class="p">{p['price']} · See the bottle</div>
      </div>
    </a>''' for p in PAGES.values())
    pixel = f"""<script>
!function(f,b,e,v,n,t,s){{if(f.fbq)return;n=f.fbq=function(){{n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)}};if(!f._fbq)f._fbq=n;
n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}}(window,
document,'script','https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '{PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"/></noscript>"""
    fbv = (f'<meta name="facebook-domain-verification" content="{META_DOMAIN_VERIFICATION}">'
           if META_DOMAIN_VERIFICATION else
           '<!-- facebook-domain-verification tag goes here once Ryan pulls the code from Business Manager -->')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Coppercraft Whiskey · Small-Batch Whiskey from Holland, Michigan</title>
<meta name="description" content="Small-batch bourbon and rye from Coppercraft Distillery in Holland, Michigan. Shipped to your door.">
<link rel="canonical" href="{BASE_URL}/">
{fbv}
<style>
{fonts}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Arial,sans-serif;background:#171310;color:#F0E6D2;min-height:100vh;line-height:1.6}}
.disp{{font-family:'Oswald','Arial Narrow',Arial,sans-serif}}
main{{max-width:640px;margin:0 auto;padding:56px 20px 40px;text-align:center}}
.logo{{height:76px;margin:0 auto 26px;display:block}}
h1{{font-family:'Oswald',Arial,sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:2px;font-size:clamp(26px,5vw,34px);margin-bottom:8px}}
.sub{{color:#C9BCA0;font-size:15px;margin-bottom:36px}}
.card{{display:flex;align-items:center;gap:18px;background:#241F1A;border:1px solid #3a322a;border-radius:12px;padding:16px 20px;margin-bottom:14px;color:#F0E6D2;text-decoration:none;text-align:left;transition:border-color .15s}}
.card:hover{{border-color:#B87333}}
.card img{{height:110px;width:auto;flex:0 0 auto}}
.card .n{{font-family:'Oswald',Arial,sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:1px;font-size:18px}}
.card .d{{color:#9b8a6f;font-size:13.5px;margin-top:3px}}
.card .p{{color:#B87333;font-family:'Oswald',Arial,sans-serif;font-weight:600;letter-spacing:1px;text-transform:uppercase;font-size:13.5px;margin-top:8px}}
footer{{max-width:640px;margin:0 auto;padding:10px 20px 48px;text-align:center;color:#9b8a6f;font-size:12.5px}}
footer .resp{{font-family:'Oswald',Arial,sans-serif;letter-spacing:2.5px;font-size:12px;color:#C9BCA0;margin-bottom:14px}}
footer div{{margin-bottom:6px}}
footer a{{color:#9b8a6f}}
#age{{position:fixed;inset:0;z-index:100;background:rgba(16,12,8,.96);display:flex;align-items:center;justify-content:center;padding:20px}}
#age .box{{background:#F2EDE3;border-radius:12px;max-width:420px;width:100%;padding:38px 30px;text-align:center;color:#2b241d}}
#age img{{height:64px;margin:0 auto 18px;display:block;filter:invert(1) brightness(.2)}}
#age h2{{font-family:'Oswald',Arial,sans-serif;font-weight:600;text-transform:uppercase;letter-spacing:1px;font-size:24px;margin-bottom:8px}}
#age p{{font-size:14px;color:#5d5245;margin-bottom:22px}}
#age .row{{display:flex;gap:10px}}
#age button{{flex:1;padding:13px;border-radius:6px;border:0;cursor:pointer;font-family:'Oswald',Arial,sans-serif;font-weight:600;font-size:15px;letter-spacing:1px;text-transform:uppercase}}
#age .yes{{background:#B87333;color:#fff}}
#age .no{{background:#DCD2BE;color:#241F1A}}
body.gated{{overflow:hidden}}
</style>
{pixel}
</head>
<body>
<div id="age">
  <div class="box">
    <img src="assets/logo-white.png" alt="Coppercraft Distillery">
    <h2>Are you 21 or older?</h2>
    <p>You must be of legal drinking age to enter this site.</p>
    <div class="row">
      <button class="yes" onclick="ageYes()">Yes, I'm 21+</button>
      <button class="no" onclick="ageNo()">No</button>
    </div>
  </div>
</div>
<main>
  <img class="logo" src="assets/logo-white.png" alt="Coppercraft Distillery">
  <h1>Coppercraft Whiskey</h1>
  <p class="sub">Small-batch whiskey from Holland, Michigan. Shipped to your door.</p>
  {cards}
</main>
<footer>
  <div class="resp">DRINK RESPONSIBLY · 21+</div>
  <div><a href="{PRIVACY_URL}">Terms &amp; Privacy</a></div>
  <div>{esc(FLAVIAR_LINE)}</div>
  <div>{esc(SHIP_NOTE)}</div>
  <div>© 2026 Coppercraft Distillery · Holland, Michigan · Est. 2012</div>
</footer>
<script>
(function(){{
  var gate=document.getElementById('age');
  try{{ if(localStorage.getItem('cc21')==='1'){{gate.remove();}} else {{document.body.classList.add('gated');}} }}catch(e){{document.body.classList.add('gated');}}
  window.ageYes=function(){{try{{localStorage.setItem('cc21','1');}}catch(e){{}} gate.remove(); document.body.classList.remove('gated');}};
  window.ageNo=function(){{window.location.href='https://www.responsibility.org/';}};
}})();
</script>
</body>
</html>"""


REDIRECT_STUB = """<!DOCTYPE html><html><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=/{slug}/"><link rel="canonical" href="/{slug}/">
<title>Redirecting</title></head><body><a href="/{slug}/">Continue</a></body></html>"""

if __name__ == "__main__":
    for key in PAGES:
        fname, doc = render(key)
        slug = fname.replace(".html", "")
        # clean-path build: /<slug>/index.html with ../ asset refs
        doc = (doc.replace('src="assets/', 'src="../assets/')
                  .replace("'assets/", "'../assets/"))
        outdir = HERE / slug
        outdir.mkdir(exist_ok=True)
        (outdir / "index.html").write_text(doc)
        # legacy flat URL redirects to the clean path
        (HERE / fname).write_text(REDIRECT_STUB.format(slug=slug))
        print(f"wrote {slug}/index.html ({len(doc)//1024} KB) + {fname} redirect")
    hub = render_hub()
    (HERE / "index.html").write_text(hub)
    print(f"wrote index.html hub ({len(hub)//1024} KB)")

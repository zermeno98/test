import sys
from playwright.sync_api import sync_playwright
from pathlib import Path
out=Path(sys.argv[1]).resolve()
with sync_playwright() as p:
    b=p.chromium.launch(headless=True)
    for f in sorted(out.glob('*.html')):
        pg=b.new_page(viewport={'width':1000,'height':800}, device_scale_factor=2)
        pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1500)
        el=pg.query_selector('svg'); el.screenshot(path=str(out/(f.stem+'.png')))
        # medir texto vs cajas: reportar texts cuyo bbox excede el rect contenedor más cercano
        rep=pg.evaluate("""()=>{
          const svg=document.querySelector('svg'); const rects=[...svg.querySelectorAll('rect')].filter(r=>r.getAttribute('rx')=='6' && r.getAttribute('fill')!=='#f5f5f5');
          const bad=[];
          svg.querySelectorAll('text').forEach(tx=>{
            const bb=tx.getBBox(); const cx=bb.x+bb.width/2, cy=bb.y+bb.height/2;
            const host=rects.filter(r=>{const x=+r.getAttribute('x'),y=+r.getAttribute('y'),w=+r.getAttribute('width'),h=+r.getAttribute('height'); return cx>x&&cx<x+w&&cy>y&&cy<y+h;}).sort((a,b)=>a.getAttribute('width')-b.getAttribute('width'))[0];
            if(host){const x=+host.getAttribute('x'),w=+host.getAttribute('width'); if(bb.x<x+8||bb.x+bb.width>x+w-8) bad.push([tx.textContent, Math.round(bb.x-x), Math.round(x+w-(bb.x+bb.width))]);}
          });
          return bad;}""")
        print(f.stem, 'texto fuera de margen:', rep)
        pg.close()
    b.close()

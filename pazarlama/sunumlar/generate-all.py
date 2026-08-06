#!/usr/bin/env python3
"""MD → HTML deck + PDF — toplu üretici"""
import subprocess, json, os, re

OUT = "/Users/murat/Desktop/youtube/kamuyz-agent-starter/pazarlama/sunumlar/decks"
PDF = "/Users/murat/Desktop/youtube/kamuyz-agent-starter/pazarlama/sunumlar/pdf"
os.makedirs(OUT, exist_ok=True)
os.makedirs(PDF, exist_ok=True)

CSS = """<style>
  :root{--bg:#0D0D0D;--text:#f1f5f9;--accent:#D4856A;--muted:#94a3b8;--border:rgba(255,255,255,0.08);--card:rgba(255,255,255,0.03)}
  *{margin:0;padding:0;box-sizing:border-box}
  body{background:var(--bg);color:var(--text);font-family:'Outfit',system-ui,sans-serif;display:flex;justify-content:center;padding:40px}
  .page{width:1000px;padding:60px 70px;border:1px solid var(--border);border-radius:20px}
  .k{font-size:13px;letter-spacing:5px;text-transform:uppercase;color:var(--accent);margin-bottom:16px;font-family:'Space Mono',monospace}
  h1{font-size:52px;font-weight:800;line-height:1.1;margin-bottom:12px}
  h2{font-size:32px;font-weight:700;color:var(--accent);margin:30px 0 12px}
  h3{font-size:22px;font-weight:600;margin:16px 0 8px}
  p,li{font-size:16px;line-height:1.7;color:var(--muted)}
  ul,ol{padding-left:20px;margin:8px 0}
  .bar{width:60px;height:3px;background:var(--accent);margin:16px 0 28px}
  .box{border:1px solid var(--border);border-radius:12px;padding:20px;margin:12px 0;background:var(--card)}
  .grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:12px 0}
  table{width:100%;border-collapse:collapse;margin:16px 0}
  th{text-align:left;padding:10px 14px;border-bottom:2px solid rgba(212,133,106,0.3);font-size:16px;color:var(--accent)}
  td{padding:10px 14px;border-bottom:1px solid rgba(255,255,255,0.05);font-size:15px;color:var(--muted)}
  blockquote{border-left:3px solid var(--accent);padding:12px 18px;margin:12px 0;background:rgba(212,133,106,0.05);border-radius:0 8px 8px 0;font-style:italic}
  code{font-family:'Space Mono',monospace;font-size:14px;background:rgba(255,255,255,0.06);padding:2px 6px;border-radius:4px}
  pre{background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:10px;padding:20px;overflow-x:auto;margin:12px 0;font-size:14px;font-family:'Space Mono',monospace}
  .footer{margin-top:30px;padding-top:20px;border-top:1px solid var(--border);font-size:13px;color:var(--muted)}
  @media print{body{background:#fff;color:#000}.page{border-color:#ccc}}
</style>"""

SCRIPT = """<script>document.querySelectorAll('a').forEach(a=>{if(a.href&&!a.href.startsWith('http'))a.href='https://github.com/murataslan1/kamuyz-agent-starter/blob/main/'+a.href.split('/').slice(-3).join('/')})</script>"""

def md_to_html(md_path, slug):
    with open(md_path) as f:
        content = f.read()
    
    # Extract title from first heading
    title = ""
    for line in content.split('\n'):
        m = re.match(r'^#\s+(.+)', line)
        if m:
            title = m.group(1)
            break
    
    # Kick start - second heading or description
    kicker = ""
    for line in content.split('\n'):
        m = re.match(r'^##\s+(.+)', line)
        if m and 'İçindekiler' not in m.group(1):
            kicker = m.group(1)
            break
    
    # Convert basic MD to HTML
    html = content
    # Headings
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    # Italic
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    # Code blocks
    html = re.sub(r'```(.+?)```', r'<pre>\1</pre>', html, flags=re.DOTALL)
    # Inline code
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    # Links
    html = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', html)
    # Lists
    html = re.sub(r'^(\s*)- (.+)$', r'<li>\2</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\n\g<0>\n</ul>', html)
    # Blockquotes
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    # Paragraphs
    paragraphs = []
    for block in html.split('\n\n'):
        block = block.strip()
        if not block: continue
        if block.startswith('<h') or block.startswith('<ul') or block.startswith('<pre') or block.startswith('<table') or block.startswith('<blockquote'):
            paragraphs.append(block)
        else:
            paragraphs.append(f'<p>{block}</p>')
    
    body = '\n'.join(paragraphs)
    body = body.replace('</ul>\n<ul>', '')
    
    # Wrap in template
    deck = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8"><title>{title}</title>
{CSS}
</head>
<body>
<div class="page">
<div class="k">{kicker or slug.replace('-',' ').title()}</div>
{body}
<div class="footer"><p>github.com/murataslan1/kamuyz-agent-starter</p></div>
</div>
{SCRIPT}
</body>
</html>"""
    
    html_path = f"{OUT}/{slug}.html"
    with open(html_path, 'w') as f:
        f.write(deck)
    return html_path

# Key files to process
files = {
    "b2b-satis-rehberi.md": "b2b-satis-rehberi",
    "kamukod-210/faq.md": "kamukod-210-faq",
    "kamukod-210/comparison.md": "kamukod-210-karsilastirma",
    "kamukod-210/landing.md": "kamukod-210-landing",
    "b2b-use-cases.md": "b2b-use-cases",
    "referans/hermes-hizli-referans.md": "hermes-referans",
}

BASE = "/Users/murat/Desktop/youtube/kamuyz-agent-starter/pazarlama"
paths = []

for file, slug in files.items():
    full_path = f"{BASE}/{file}"
    if os.path.exists(full_path):
        print(f"  {file} → {slug}.html")
        html_path = md_to_html(full_path, slug)
        paths.append(html_path)
        print(f"    ✓ {html_path}")
    else:
        print(f"  ✗ {file} bulunamadı")

# Generate PDFs from all HTML decks
print("\n  PDF üretiliyor...")
script = f"""
const {{ chromium }} = require('playwright-core');
(async () => {{
  const browser = await chromium.launch({{ headless: true }});
  const files = {json.dumps([(p, p.replace('/decks/','/pdf/').replace('.html','.pdf')) for p in paths])};
  for (const [src, out] of files) {{
    const page = await browser.newPage();
    await page.goto('file://' + src, {{ waitUntil: 'networkidle' }});
    await page.pdf({{ path: out, width: '1000px', printBackground: true }});
    console.log('    ✓ ' + out.split('/').pop());
    await page.close();
  }}
  await browser.close();
}})();
"""

result = subprocess.run(['node', '-e', script], capture_output=True, text=True, cwd=BASE)
print(result.stdout)
if result.stderr: print(result.stderr[:300])

print(f"\n✓ HTML'ler: {OUT}/")
print(f"✓ PDF'ler: {PDF}/")

#!/usr/bin/env python3
"""Toplu HTML deck → PDF dönüştürücü"""
import subprocess, json, os, glob

SRC = "/Users/murat/Desktop/youtube/kamuyz-agent-starter/pazarlama/sunumlar"
PDF = f"{SRC}/pdf"
os.makedirs(PDF, exist_ok=True)

# Tüm HTML dosyalarını bul
html_files = []
for root, dirs, files in os.walk(SRC):
    for f in files:
        if f.endswith('.html') and 'node_modules' not in root:
            html_files.append(os.path.join(root, f))

script = f"""
const {{ chromium }} = require('playwright-core');
(async () => {{
  const browser = await chromium.launch({{ headless: true }});
  const files = {json.dumps([(f, f.replace('.html','.pdf').replace('/sunumlar/','/sunumlar/pdf/')) for f in html_files])};
  for (const [src, out] of files) {{
    try {{
      const page = await browser.newPage();
      await page.goto('file://' + src, {{ waitUntil: 'networkidle', timeout: 10000 }});
      await page.pdf({{ path: out, width: '1280px', height: '720px', printBackground: true }});
      console.log('  ✓ ' + out.split('/').pop());
      await page.close();
    }} catch(e) {{ console.log('  ✗ ' + src.split('/').pop() + ': ' + e.message); }}
  }}
  await browser.close();
  console.log('\\n✓ Toplam: ' + files.length + ' PDF');
}})();
"""

result = subprocess.run(['node', '-e', script], capture_output=True, text=True, cwd=SRC)
print(result.stdout)
if result.stderr: print(result.stderr[:500])

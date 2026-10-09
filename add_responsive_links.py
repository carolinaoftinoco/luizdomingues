from pathlib import Path
import re
base = Path('links')
html_files = sorted(base.glob('*.html'))
updated = []
skipped = []
for path in html_files:
    text = path.read_text(encoding='utf-8')
    if 'responsivo.css' in text:
        skipped.append(path.name)
        continue
    pattern = r'(<link rel="stylesheet" href="\.\./src/css/estilos\.css"/?>(?:\r?\n)?)'
    replacement = r'\1<link rel="stylesheet" href="../src/css/responsivo.css"/>\1'
    new_text = re.sub(pattern, replacement, text, count=1)
    if new_text == text:
        skipped.append(path.name)
    else:
        path.write_text(new_text, encoding='utf-8')
        updated.append(path.name)
print('UPDATED', updated)
print('SKIPPED', skipped)

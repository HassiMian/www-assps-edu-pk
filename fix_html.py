import sys

with open('c:/projects/My SAas/apex-web/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<div class="ld-ring"></div>\n    <div class="ld-ring"></div>\n', '')
content = content.replace('src="LOGO_SRC"', 'src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"')
content = content.replace('document.querySelectorAll(\'[src="LOGO_SRC"]\').forEach(el => el.src = logoSrc);', 'document.querySelectorAll(\'#loaderLogo, #navLogo, #footerLogo\').forEach(el => el.src = logoSrc);')
content = content.replace('document.getElementById(\'loaderLogo\') && (document.getElementById(\'loaderLogo\').src = logoSrc);', '')

with open('c:/projects/My SAas/apex-web/index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('File updated successfully.')

import os

file_path = r'c:\projects\My SAas\apex-web\index.html'

with open(file_path, 'rb') as f:
    content = f.read()

# Fix Mojibake En-dash (â€“ -> –)
content = content.replace(b'\xc3\xa2\xc2\x80\xc2\x93', b'-')
# Fix Mojibake Bullet/Emoji (ðŸŒŸ -> *)
content = content.replace(b'\xc3\xb0\xc5\xb8\xc5\x92\xc5\xb8', b'*')

# Parse as text to replace src="" with transparent GIF
text = content.decode('utf-8', errors='replace')

text = text.replace('src=""', 'src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"')

# Also remove any stray "ðŸŒŸ" that might be plain UTF-8 encoded
text = text.replace('ðŸŒŸ', '*')
text = text.replace('â€“', '-')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("index.html fixed!")

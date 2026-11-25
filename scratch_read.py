with open('index.html', encoding='utf-8') as f:
    text = f.read()

print('Has s2:', 'id="s2"' in text)
print('Has s3 (20+):', 'id="s3"' in text, '20+' in text)
print('Has s4:', 'id="s4"' in text)
print('Has s9:', 'id="s9"' in text)

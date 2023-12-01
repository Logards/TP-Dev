import base64

file = open('hampter.jpg', 'rb')
content = file.read()
file.close()
print(content)
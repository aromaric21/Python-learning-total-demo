from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

data = open("data.txt", "rb").read()
enc = f.encrypt(data)
open('secret.txt', 'wb').write(enc)
print('Locked ! key :', key.decode())
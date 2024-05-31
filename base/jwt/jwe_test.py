from jose import jwe
from cryptography.hazmat.primitives import hmac, hashes
from cryptography.hazmat.backends import default_backend

# Generate a 128-bit key for AES-GCM
# key = 'asecret128bitkey'
key = b'\x10\xf5?\x1b\x8ci\xcb1\xf6\x06<"xb\x9eh'

encr=jwe.encrypt('Hello, World!', key, algorithm='dir', encryption='A128GCM')

print(encr)

decr= jwe.decrypt(encr, key)

print(decr)
from jose import jwe
from jose.constants import ALGORITHMS
import os

# Generate a random 128-bit content encryption key (CEK)
cek = os.urandom(16)

cekstr :str=cek
print('cek key= ', cek)
print('cekstr key= ', cekstr)



# Define your payload
payload='Hello world'
# payload = {
#     "sub": "1234567890",
#     "name": "John Doe",
#     "iat": 1516239022
# }

# Encrypt the payload using the CEK and A128GCM algorithm
encrypted_payload = jwe.encrypt(payload,  cekstr, algorithm=ALGORITHMS.A128GCM)

print("Encrypted Payload:", encrypted_payload)

decr= jwe.decrypt(encrypted_payload, cekstr)

print(decr)
print('cek key= ', cekstr)

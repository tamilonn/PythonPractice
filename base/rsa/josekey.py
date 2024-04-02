import base64
import json

try:
    from jose.backends import rsa_backend
    from jose.backends.rsa_backend import RSAKey as PurePythonRSAKey
except ImportError:
    PurePythonRSAKey = rsa_backend = None

try:
    from Crypto.PublicKey import RSA as PyCryptoRSA
except ImportError:
    PyCryptoRSA = None


try:
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives.asymmetric import rsa as pyca_rsa

    from jose.backends.cryptography_backend import CryptographyRSAKey
except ImportError:
    default_backend = pyca_rsa = CryptographyRSAKey = None

from jose.backends import RSAKey
from jose.constants import ALGORITHMS
from jose.exceptions import JOSEError, JWKError

import rsa


def generate_keypair():

    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key

public_key, private_key = generate_keypair()

#TODO

def genjwk():
    key = PurePythonRSAKey(private_key, ALGORITHMS.RS256)
    return key


mykey = genjwk()
print(mykey)
print('-----------------------------------')
new_pem = mykey.to_pem(pem_format="PKCS8")
print(new_pem)
print('-----------------------------------')

pubkey = mykey.public_key
print(pubkey)
print('-----------------------------------')
configurations
	
  "":"",
  "":"",
  "":"",
  "":"",
  "":"",
  "":""
{
  "success": true,
  "apiversion": "1.0",
  "data": {
        "algorithm" : "RSA256",
          "application":"credit card service",
          "token_expiration_time": 1200,
          "signkey_rotate_time":7776000,
          "kill_jwt": "False",
          "comments":"This is credit card service"
        "config_id":"123456789",
        "action":"SAVE",
        "internal":"True",
        "organization":"jaykrishco",
        "created_date":"2024-04-02 12:30:888",
        "updated_date":"2024-04-02 12:30:888"
  },
  "error": null
}

{
  "algorithm" : "RSA256",
  "application":"credit card service",
  "token_expiration_time": 1200,
  "signkey_rotate_time":7776000,
  "kill_jwt": "False",
  "comments":"This is credit card service"
  "config_id":"123456789",
  "action":"SAVE",
  "internal":"True",
  "organization":"jaykrishco",
  "created_date":"2024-04-02 12:30:888",
  "updated_date":"2024-04-02 12:30:888"
}


key = RSAKey(private_key, ALGORITHMS.RS256)
print(key)

# token = "eyJhbGciOiJIUzI1NiIsImtpZCI6IjAxOGMwYWU1LTRkOWItNDcxYi1iZmQ2LWVlZjMxNGJjNzAzNyJ9.SXTigJlzIGEgZGFuZ2Vyb3VzIGJ1c2luZXNzLCBGcm9kbywgZ29pbmcgb3V0IHlvdXIgZG9vci4gWW91IHN0ZXAgb250byB0aGUgcm9hZCwgYW5kIGlmIHlvdSBkb24ndCBrZWVwIHlvdXIgZmVldCwgdGhlcmXigJlzIG5vIGtub3dpbmcgd2hlcmUgeW91IG1pZ2h0IGJlIHN3ZXB0IG9mZiB0by4.s0h6KThzkfBBBkLspW1h84VsJZFTsPPqMDA7g1Md7p0"
# >>> hmac_key = {
#     "kty": "oct",
#     "kid": "018c0ae5-4d9b-471b-bfd6-eef314bc7037",
#     "use": "sig",
#     "alg": "HS256",
#     "k": "hJtXIZ2uSN5kbQfbtTNWbpdmhkV8FJG-Onbc6mxCcYg"
# }
# >>>
# >>> key = jwk.construct(hmac_key)
# >>>
# >>> message, encoded_sig = token.rsplit('.', 1)
# >>> decoded_sig = base64url_decode(encoded_sig)
# >>> key.verify(message, decoded_sig)
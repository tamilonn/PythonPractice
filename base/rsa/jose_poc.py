import json
from jwcrypto.jwk import JWK, JWKSet
from jose.constants import ALGORITHMS
from jose import jwt
from jose import jwe
import os
from time import time
from jose import jwe


try:
    from jose.backends.rsa_backend import RSAKey
except ImportError:
    PurePythonRSAKey = rsa_backend = None

'Ths POC is for jwt token create and verify using RSA256 algorithm'
'Also encrypt/decrypt the RSAKey so that it can be stored in database as bytes'


def generate_rsa256_keypair(kid)-> RSAKey:
    jwkpair = JWK.generate(kty='RSA', size=2048, kid=kid, use='sig', alg='RS256')
    key = RSAKey(jwkpair, ALGORITHMS.RS256)
    return key



def sign_and_verify_jwt(jwk: RSAKey):

    expiry = int(time()) + 2400

    payload_data = {
        "sub": "tamilonn",
        "name": "Jessica Temporal",
        "nickname": "Jess",
        "exp": expiry,
        "iss": "jaykrishco",
        "nbf": 1715148460,
        "iat": 1715148460,
        "jti": "jti11111",
        "aud": "credit card service"
    }

    headers = {
        "kid": KID    
    }

    new_token = jwt.encode(claims=payload_data, headers=headers, key=jwk,  algorithm='RS256')

    print('   new token is : ', new_token)

    payload = jwt.decode(
        new_token,
        key=jwk.public_key(),
        algorithms=["RS256", ],
        audience="credit card service"

    )

    print('   payload is : ', payload)


def cek_generate(size: int=32):
    'Generate a random 256-bit content encryption key (CEK)'
    '16-A128GCM / 24-A192GCM / 32-A256GCM pairs are allowed for key generation and encryption'
    cek = os.urandom(size)
    return cek


def encrypt(data: bytes, key:bytes, algorithm='dir', encryption='A256GCM')-> bytes:

    encrypted =jwe.encrypt(data, key, algorithm=algorithm, encryption=encryption)
    return encrypted


def decrypt(data: bytes, key:bytes)-> bytes:
    decrypted = jwe.decrypt(data, key)
    return decrypted




def encrypt_rsakey(jwk: RSAKey, key: bytes):
    key_pem = jwk.to_pem(pem_format="PKCS8")
    # str_key_pem = str(key_pem, encoding='utf-8')
    return encrypt(key_pem, key)

def load_rsaKey(data: bytes)-> RSAKey:
    key = RSAKey(data, ALGORITHMS.RS256)
    return key




def decrypt_rsakey(data: bytes, key: bytes)-> bytes:
    return jwe.decrypt(data, key)




if __name__ == '__main__':
    KID = "mykeyid123"

    # Generate a 128-bit key for AES-GCM
    # key = 'asecret128bitkey'
    key = cek_generate() #16 or 24 or 32(default)

    jwk = generate_rsa256_keypair(KID)
    print(jwk)
    # pubkey = jwkpair.export_public(as_dict=True)
    # privkey = jwkpair.export_private(as_dict=True)

    #Test
    sign_and_verify_jwt(jwk)

    enc_rsakey = encrypt_rsakey(jwk, key)

    decr_rsakey = decrypt_rsakey(enc_rsakey, key)

    new_rsakey = load_rsaKey(decr_rsakey)

    #Test
    sign_and_verify_jwt(new_rsakey)





    # JWKSet preparation....................................................

    jwk = generate_rsa256_keypair(kid='mykid1')
    enc_rsakey = encrypt_rsakey(jwk, key)
    decr_rsakey = decrypt_rsakey(enc_rsakey, key)
    new_rsakey = load_rsaKey(decr_rsakey)

    # pkdict = new_rsakey.public_key().to_dict()
    pkdict = jwk.public_key().to_dict()
    prikdict = jwk.to_dict()
    print('public key in dict= ' ,prikdict)



    myjwk = JWK.from_json(json.dumps(pkdict))
    # print('myjwk === ', myjwk)

    #JWKSet generation:
    jwtkeys: dict[str,list]={}
    keys = "keys"
    keylist: list = []

    keylist.append(myjwk)
    jwtkeys[keys] = keylist
    myjwkset = JWKSet.from_json(json.dumps(jwtkeys))

    print('Final JWKSet object is .... ', myjwkset)

    print('COnclusion: Since JOSE RSAKey do not carry "kid" attribute, we cannot use RSAKey. ')

 





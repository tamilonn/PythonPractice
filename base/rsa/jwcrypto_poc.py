
import json
from jwcrypto.jwk import JWK, JWKSet
from jose.constants import ALGORITHMS
from jose import jwt
from jose import jwe
import os
from time import time
from jose import jwe

"""
This is a POC for JWT signing/ verifying
Also Encrypt, Decrypt JWK object 
"""
'Generate JWK'
def generate_rsa256_keypair(kid)-> JWK:
    jwk = JWK.generate(kty='RSA', size=2048, kid=kid, use='sig', alg='RS256')
    return jwk

'Generate key for encryption of JWK'
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




def encrypt_rsakey(jwk: JWK, key: bytes):
    """
    Convert the JWK to bytes as PEM (PKCS8 format)
    Encrypt the JWK with password
    """
    key_pem = jwk.export_to_pem(private_key=True, password=None)
    return encrypt(key_pem, key)


def decrypt_rsakey(data: bytes, key: bytes)-> bytes:
    """
    Decrypt the bytes to get JWK
    """
    return jwe.decrypt(data, key)

#Test the JWK for Jwt sign and verify
def sign_and_verify_jwt(jwk: JWK)-> str:

    expiry = int(time()) + 2400

    payload_data = {
        "sub": "tamilonn",
        "name": "Tamilselvan Radhakrishnan",
        "nickname": "Jess",
        "exp": expiry,
        "iss": "jaykrishco",
        "nbf": 1715148460,
        "iat": 1715148460,
        "jti": "jti11111",
        "aud": "credit card service"
    }

    headers = {
        "kid": "jwcryptopockeyid123"    
    }

    new_token = jwt.encode(claims=payload_data, headers=headers, key=jwk,  algorithm='RS256')

    payload = jwt.decode(
        new_token,
        key=jwk.export_public(as_dict=True),
        algorithms=["RS256", ],
        audience="credit card service"

    )

    print('   payload is : ', payload)
    return new_token

if __name__ == '__main__':
    KID = "jwcryptopockeyid123"

    # Generate a 128-bit key for AES-GCM
    # key = 'asecret128bitkey'
    key = cek_generate() #16 or 24 or 32(default)

    jwk = generate_rsa256_keypair(KID)

    # pubkey = jwkpair.export_public(as_dict=True)
    # privkey = jwkpair.export_private(as_dict=True)

    #Test
    sign_and_verify_jwt(jwk)

    enc_rsakey = encrypt_rsakey(jwk, key)

    decr_rsakey = decrypt_rsakey(enc_rsakey, key)

    new_rsakey = JWK.from_pem(decr_rsakey)

    print("new JWK= ", new_rsakey.export())

    new_rsakey.update(kid='jwcryptopockeyid123')

    print("KID updated JWK = ", new_rsakey.export())

    jwttoken = sign_and_verify_jwt(new_rsakey)

    #verify token using JWKSet public key
    """
    JWKSet is required to generate public keys so that client can verify token RSA way
    To generate JWKSet, we will follow the below steps:
    """
    jwtkeys: dict[str,list]={}
    keys = "keys"
    keylist: list = []

    publicKey= new_rsakey.export_public(as_dict=True)

    myjwk = JWK.from_json(json.dumps(publicKey))
    keylist.append(myjwk)
    # here we could add more JWK for another JWK if available

    jwtkeys[keys] = keylist

    # Generate JWKSet object from keys json
    myjwkset = JWKSet.from_json(json.dumps(jwtkeys))

    testkid= "jwcryptopockeyid123"
    pubjwk = myjwkset.get_key(testkid)

    payload = jwt.decode(
        jwttoken,
        key=pubjwk,
        algorithms=["RS256", ],
        audience="credit card service")

    print(payload)

    print('conclusion:   jwcrypto is good for using sign/verify JWT token since it support JWKSet with "kid" searching public key (JWK).  Hence we will use JWK instead of RSAKey')


    
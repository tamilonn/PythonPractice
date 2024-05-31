from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

private_key_pass = b"your-password"

encrypted_pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(private_key_pass)
)

print(encrypted_pem_private_key.splitlines()[0])
# b'-----BEGIN ENCRYPTED PRIVATE KEY-----'

unencrypted_pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
)

print(unencrypted_pem_private_key.splitlines()[0])
# b'-----BEGIN RSA PRIVATE KEY-----'

pem_public_key = private_key.public_key().public_bytes(
  encoding=serialization.Encoding.PEM,
  format=serialization.PublicFormat.SubjectPublicKeyInfo
)

print(pem_public_key.splitlines()[0])



# def genjwk():
#     # key = PurePythonRSAKey(privkey, ALGORITHMS.RS256)
#     key = PurePythonRSAKey(jwkpair, ALGORITHMS.RS256)
#     return key


# print(' JWCRYPTO ends...............................................')



# print('---------------------------------------------')

# print('------------------JOSE RSA starts ...---------------------------')

# def genjwk():
#     # key = PurePythonRSAKey(privkey, ALGORITHMS.RS256)
#     key = PurePythonRSAKey(jwkpair, ALGORITHMS.RS256)
#     return key

# jose_jwk = genjwk()

# mytoken = jwt.encode(claims=payload_data, headers=headers, key=jose_jwk,  algorithm='RS256')

# print('mytoken = ', mytoken)


# mypayload = jwt.decode(
#     mytoken,
#     key=jose_jwk.public_key(),
#     algorithms=["RS256", ],
#     audience="credit card service"

# )
# print('mypayload= ', mypayload)
# print('public key= ', jose_jwk.public_key())

# publickeycert = jose_jwk.public_key().to_dict()
# print('publickeycert = ',publickeycert)

# print('---------------- jose_jwk ----------------------------------')
# print('jose_jwk = ',jose_jwk)
# print('---------------- ends jose_jwk ----------------------------------')
# print('--------------------------------------------------')

# print('storing RSA keys to storage.........................................')
# new_pem = jose_jwk.to_pem(pem_format="PKCS8")
# print('new_pem (PKCS8)  =', new_pem)

# print('End storing RSA keys to storage.........................................')
# print('--------------------------------------------------')

# print('-----------Convert PEM bytes to RSA KEY---------------------------------------')

# loaded_jose_jwk = RSAKey(new_pem, ALGORITHMS.RS256)
# print('loaded_jose_jwk =', loaded_jose_jwk)

# loadedtoken = jwt.encode(claims=payload_data, headers=headers, key=loaded_jose_jwk,  algorithm='RS256')

# print('loadedtoken = ', loadedtoken)


# loadedpayload = jwt.decode(
#     mytoken,
#     key=loaded_jose_jwk.public_key(),
#     algorithms=["RS256", ],
#     audience="credit card service"

# )
# print('loadedpayload = ', loadedpayload)

# print('-----------End Convert PEM bytes to RSA KEY---------------------------------------')

# print('------------------Password protecting bytes pem------------------')

# strPEM : str = str(new_pem, encoding='utf-8')

# print('strPEM = ', strPEM)

# from jose import jwe
# encr=jwe.encrypt(strPEM, 'asecret128bitkey', algorithm='dir', encryption='A128GCM')

# print('encrypted strPEM = ', encr)

# decrPEM= jwe.decrypt(encr, 'asecret128bitkey')

# print('Decrypted PEM= ', decrPEM)

# print('***************** REDOING JWT creation and verification *****************************************')


# decrypted_jose_jwk = RSAKey(decrPEM, ALGORITHMS.RS256)
# print('decrypted_jose_jwk =', decrypted_jose_jwk)

# decr_loadedtoken = jwt.encode(claims=payload_data, headers=headers, key=decrypted_jose_jwk,  algorithm='RS256')

# print('decr_loadedtoken = ', decr_loadedtoken)


# decr_loadedpayload = jwt.decode(
#     mytoken,
#     key=decrypted_jose_jwk.public_key(),
#     algorithms=["RS256", ],
#     audience="credit card service"

# )
# print('decr_loadedpayload = ', decr_loadedpayload)

# print('-----------End Encryption and decryption of RSA Key ---------------------------------------')










# public interface PublicClaims {

#     //Header
#     String ALGORITHM = "alg";
#     String CONTENT_TYPE = "cty";
#     String TYPE = "typ";
#     String KEY_ID = "kid";

#     //Payload
#     String ISSUER = "iss";
#     String SUBJECT = "sub";
#     String EXPIRES_AT = "exp";
#     String NOT_BEFORE = "nbf";
#     String ISSUED_AT = "iat";
#     String JWT_ID = "jti";
#     String AUDIENCE = "aud";
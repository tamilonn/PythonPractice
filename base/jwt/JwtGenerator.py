print('creating and verifying JWT token')

secret = 'abc123@'


def createJwt(dictionary):

    from jose import jwt
    token = jwt.encode(dictionary, secret, algorithm='HS256')

    # print(token)

    return token






    

def verifyJwt(jwtToken):

    from jose import jwt

    verified = jwt.decode(jwtToken, secret, algorithms=['HS256'])

    return verified

  




# from jose import jwt
# token = jwt.encode({'key': 'value'}, 'secret', algorithm='HS256')

# print(token)
    
# iss - Issuer
# sub - Subject
# aud - Audience
# exp - Expiration Time
# nbf - Not Before
# iat - Issued At
# jti - JWT ID

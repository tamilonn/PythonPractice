
def start():
    # This program calls JwtGenerator.py to create new JWT and verify JWT token

    from calendar import timegm

    from datetime import datetime, timedelta



    #Prepare a dictionary with claims value for jwt

    exp_time = timegm(datetime.utcnow().utctimetuple()) + 100

    # exp_time = 10
    issued_at = timegm(datetime.utcnow().utctimetuple())

    print('issued_at = '+ str(issued_at))

    claims = {
        "sub" : "tarunkrishacc@gmail.com",
        "iss" : "jaykrishco.com",
        # "aud" : "none",
        "exp" : exp_time,
        # "nbf" : "none",
        "iat" : issued_at,
        "jti" : "xyzid",


    }

    print(claims)

    print('------ calling createJwt ------------')

    from JwtGenerator import createJwt, verifyJwt

    jwtToken = createJwt(claims)

    print(jwtToken)

    print('now verifying jwt token----------------')

    verified = '';
    # verified = verifyJwt(jwtToken)

    try:
        verified = verifyJwt(jwtToken)
    except Exception as err:
        print(err)

    print(verified)



if (__name__ == '__main__'):
    start()


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

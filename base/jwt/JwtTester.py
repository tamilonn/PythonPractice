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

verified = ''
# verified = verifyJwt(jwtToken)

try:
  verified = verifyJwt(jwtToken)
except Exception as err:
  print(err)
  



print(verified)
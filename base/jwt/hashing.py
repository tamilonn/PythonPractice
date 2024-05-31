from passlib.context import CryptContext
import logging

# Hide the warning message coming from bcrypt
logging.getLogger('passlib').setLevel(logging.ERROR)

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)

    def verify(hashed_password,plain_password):
        return pwd_cxt.verify(plain_password,hashed_password)
    


# if __name__ == '__main__':
    
#     encrypted = Hash.bcrypt('pwd1231')
#     print(encrypted)


#     decryped = Hash.verify(encrypted, 'pwd1231')
#     print(decryped)
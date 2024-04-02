import rsa


def generate_keypair():

    public_key, private_key = rsa.newkeys(2048)
    return public_key, private_key



def encrypt(value : str, publickey):
    message= value.encode('utf8')
    encrypted = rsa.encrypt(message, publickey) #ciphertext

    return encrypted

def decrypt(encrypted_value, privatekey):
        decrypted = rsa.decrypt(encrypted_value, privatekey)

        return decrypted


def sign(data: str, privatekey):
     
     return rsa.sign(data.encode('utf8'), privatekey, 'SHA-1')
     

def verify(data: str, signature, publickey):
     return rsa.verify(data.encode('utf8'), signature, publickey)

def sign_verify(publickey, privatekey):
     data = 'Hello World Again!'.encode('utf8')
     signature = rsa.sign(data, privatekey, 'SHA-1')
     rsa.verify(data, signature, publickey)
    #  'SHA-1'

     data2 = 'Hello World2'.encode('utf8')
     hash = rsa.compute_hash(data2, 'SHA-1')
     signature2 = rsa.sign_hash(hash, privatekey, 'SHA-1')
     print('------------ done -------------')

     print('------------ done -------------')


if __name__ == '__main__':
     
     #Generate key pair
     publickey, privatekey = generate_keypair()

     message : str = 'This is plain text message with !@#$%^&*()_'

     #encrypt message
     encrypted_message = encrypt(message, publickey)
     print(f"encrypted message={encrypted_message}")

     print('---------------------------')
     
     #decrypt message
     decrypted_message = decrypt(encrypted_message, privatekey)
    
     print(f"decrypted message= {decrypted_message.decode('utf8')}")

     #sign text
     print('---------------------------')

     sign_verify(publickey, privatekey)

     msg = 'Tamilselvan'
     signed = sign(msg, privatekey)
     print(signed)

     print('---------------------------')
     
     #verify
     verified = verify(msg, signed, privatekey)
     print(verified)

  







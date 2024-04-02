from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate RSA key pair
key = RSA.generate(2048)

# will be in PEM format and byte string type

public_key = key.publickey().export_key()
public_key = public_key.decode()     # will get converted to python string when "decode" is used
print(f'Public Key: {public_key}')    

private_key = key.export_key()
private_key = private_key.decode()   # will get converted to python string when "decode" is used
print(f'Private Key: {private_key}')   

# Message to be signed
message = b"Hello, world!"

# Sign the message
hash_func = SHA256.new(message)
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(hash_func)

# Verify the signature
hash_func = SHA256.new(message)
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(hash_func, signature)
    print("\nSignature is valid.")
except (ValueError, TypeError):
    print("\nSignature is invalid.")

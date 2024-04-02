from Crypto.PublicKey import RSA

key = RSA.generate(2048)

# will be in PEM format and byte string type

public_key = key.publickey().export_key()
print(f"Public Key: {public_key.decode()}")    # will get converted to python string when "decode" is used


private_key = key.export_key()
print(f"Private Key: {private_key.decode()}")    # will get converted to python string when "decode" is used
print()

pubkey_dict: dict = {}
pubkey_dict = key.publickey().export_key()
print()
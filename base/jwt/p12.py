from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import pkcs12, PrivateFormat

common_name = "John Doe"
password = "secret"

private_key = rsa.generate_private_key(
     public_exponent=65537,
     key_size=4096,
)

cert = x509.load_pem_x509_certificate("myCert.crt")

encryption = (
     PrivateFormat.PKCS12.encryption_builder().
     kdf_rounds(50000).
     key_cert_algorithm(pkcs12.PBES.PBESv1SHA1And3KeyTripleDESCBC).
     hmac_hash(hashes.SHA1()).build(f"{password}".encode())
)

p12 = pkcs12.serialize_key_and_certificates(
    f"{common_name}".encode(), private_key, cert, None, encryption
)


# with open(f"{common_name}.p12", "wb") as p12_file:
#     p12_file.write(p12)
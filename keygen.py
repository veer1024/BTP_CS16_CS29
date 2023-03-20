from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import serialization  
from cryptography.hazmat.primitives.asymmetric import rsa  
  
p=65537
print("Enter Public Exponent for generating key or Enter 0 to select default value(i.e. 65537) :")
pub_ex=int(input())
if pub_ex !=0:
    p=pub_ex
# save file helper  
def save_file(filename, content):  
   f = open(filename, "wb")  
   f.write(content)
   f.close()  
  
  
# generate private key & write to disk  
private_key = rsa.generate_private_key(  
    public_exponent=p,  
    key_size=2048,  
    backend=default_backend()  
)  
pem = private_key.private_bytes(  
    encoding=serialization.Encoding.PEM,  
    format=serialization.PrivateFormat.PKCS8,  
    encryption_algorithm=serialization.NoEncryption()  
)  
save_file("private.pem", pem)  
  
# generate public key  
public_key = private_key.public_key()  
pem = public_key.public_bytes(  
    encoding=serialization.Encoding.PEM,  
    format=serialization.PublicFormat.SubjectPublicKeyInfo  
)  
save_file("public.pem", pem) 
print("Key Pair Generated successfully")

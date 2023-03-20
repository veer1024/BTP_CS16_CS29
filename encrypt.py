import argparse
import rsa
import base64
parser = argparse.ArgumentParser()
#parser.add_argument("-c","--chunk_name",help="chunk of the file to encrypt...")
#parser.add_argument("-p","--public_key",help="key to encrypt the chunks...")
#args = parser.parse_args()
#chunk = args.chunk_name
#pubkey = args.public_key
#print(chunk)
#print(pubkey)


## reading data from chunk 
def encrypt(chunk,pubkey):
   f = open(chunk,'r')
   message = f.read()
   #encoded_data = base64.b64encode(message).encode('ascii')
   #print(message)
   #print(pubkey)
   #print(message)
   encMessage = rsa.encrypt(message.encode('ascii'),pubkey)
   f.close()
   return encMessage


## storing encrypted data from chunk



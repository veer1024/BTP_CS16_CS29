from Crypto.Cipher import AES
import binascii, os

def encrypt_AES_GCM(chunk, secretKey):
    print(chunk)
    print(secretKey)
    f = open(chunk,'r')
    msg = bytes(f.read(),'utf-8')
    print(msg)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg)
    return (ciphertext, aesCipher.nonce, authTag)
    #print(ciphertext)
    #return ciphertext

def decrypt_AES_GCM(file_name, secretKey):
    folder_name = file_name.split('.')[0] + '_chunks'
    print("FOLDER is "+folder_name)
    for root,dirs,files in os.walk(folder_name):
      for file in files:
          f = open('./'+folder_name+'/'+file,'r')
          encryptedMsg = eval(f.read())
          print(encryptedMsg)
          print("type of encryptedmsg: "+str(type(encryptedMsg)))
          f.close()
          (ciphertext, nonce, authTag) = encryptedMsg
          print(ciphertext)
          print("++")
          print(nonce)
          print("++")
          print(authTag)
          print("++")
          aesCipher = AES.new(secretKey.encode('utf-8'), AES.MODE_GCM, nonce)
          plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
          print("plaintext is "+str(plaintext))
          f = open(file_name,'a')
          f.write(plaintext.decode('utf-8'))
          f.close()


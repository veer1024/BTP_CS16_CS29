import os
from cryptography.hazmat.backends import default_backend  
from cryptography.hazmat.primitives import serialization  
from cryptography.hazmat.primitives.asymmetric import rsa  
import argparse
import rsa
import time
import files
import aes_encrypt
import upload
import pyfiglet
import download
import crc32
import integrity_check
#import setup
parser = argparse.ArgumentParser()
parser.add_argument("-c","--chunk_name",help="chunk of the file to encrypt...")
args = parser.parse_args()
chunk = args.chunk_name
global file_name
global private_key
global public_key

# Function to generate KeyPair

## choices and banner







def find_files(filename, search_path):
   result = []
# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

def integrity_check_begin():
    print("Enter the name of file to check integrity: ")
    filename = str(input())
    integrity_check.integrity_checker(filename.split('.')[0])
def upload_begin():
   files.split()
   filename = files.inp.split(".")[0]
   K = bytes(keys[0],'utf-8')
   with open(r"./chunks/manifest", 'r') as fp:
    lines = len(fp.readlines())-1
   #print("Enter the file name without extension that you splited : ")
   #filen=input()
   os.system('rm -rf ./chunks/manifest')
   filen = filename
   os.mkdir(filen+"_chunks")
   for i in range(lines):
    chunk='enc-'+filen+'_'+str(i+1)+'.txt'
    starttime = time.time()
    encMessage = aes_encrypt.encrypt_AES_GCM('./chunks/'+chunk,K)
    endtime = time.time()
    print("encryption time: ",str(endtime - starttime))
    f = open(r'./'+filen+'_chunks/'+chunk,'w')
    f.write(str(encMessage))
    #print(encMessage)
    f.close()
   # encMessage is in bytes, so won't concate with string
   print("THIS IS THE ENCRYPTED MESSAGE: ")
   print(encMessage)
   ## generating crc32 hashes for all the chunks
   crc32.generating_hashes(filen)
   ## uploading to cloud
   
   print("=========================================> uploading ===================>")
   upload.upload_to_aws(filen+'_chunks')
   print("===========> UPLOAD DONE!")
   print("===========> Cleaning")
   os.system('rm -rf '+filen+'_chunks')
   os.system('rm -rf chunks')
   os.system('mv '+filen+'.txt ./record_'+filen+'/')
   print("cleaning done!")
   
def download_begin():
   print("Enter the name of file to download: ")
   file_name = input()
   os.system('touch '+file_name)
   folder_name = file_name.split('.')[0] + '_chunks'
   download.download_directory('enc-files',folder_name)
   print(keys[0])
   aes_encrypt.decrypt_AES_GCM(file_name,keys[0])
   print("FILE IS "+file_name)
   print("File is ready for editing")
   os.system('rm -rf '+folder_name)
   
  
ascii_banner=pyfiglet.figlet_format("Welcome !!!")
print(ascii_banner.center(100))
print('---------------------------------------------------------------------------------------\n')
print("This is a Project on Checking Intergrity of Cloud Data")
print('---------------------------------------------------------------------------------------')
print('\033[1m' + 'Developed By : '+'\033[0m'+'\nRohit Patidar (B19CS029) \nViraj Vaishnav (B19CS016)')
print('\033[1m' + 'Supervised By : Dr. Surmila Thokchom' + '\033[0m')
print('---------------------------------------------------------------------------------------\n\n')

choice=0
f=open('keys.txt','r')
keys_str=f.read()
keys=keys_str.split(';')
f.close()
print("KEYS DONE")

while True:
    print('******************************\n')
    print('Select Your choice below :')
    print('1. Upload a new file to Cloud')
    print('2. Edit a Chunk of a existing File on Cloud')
    print('3. Check Integrity of any specific Chunk or a File')
    print('4. Download a File from cloud to local Computer From Cloud')
    print('5. Exit')
    print('------------------------------------------------------------------------------------------\n\n')
    choice=int(input("Enter Your Choice : "))
    if choice==1:
        upload_begin()
    elif choice==2:
        download_begin()
    elif choice==3:
        integrity_check_begin()
    elif choice==5:
        print('BYE BYE !!!')
        break
#---------------> choices and banner

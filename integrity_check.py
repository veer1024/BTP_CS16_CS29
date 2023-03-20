import zlib
import os
import download
import crc32
import random
"""
list_dir=os.listdir('./chunks')
list_dir.remove('manifest')
list_dir.remove('new_manifest')
count=0
no_files=len(list_dir)
new_manifest=open('./chunks/new_manifest','r')
dictionary=new_manifest.read()
hashes=eval(dictionary)
for i in range(no_files):
    with open('./chunks/'+list_dir[i]) as f:
        content=f.read()
        t=zlib.crc32(bytes(content,'utf-8'))
        get_hash=hashes.get(list_dir[i])
        if t==get_hash:
            print('Integrity verified for '+ list_dir[i])
        f.close()
print('Process Completed')
"""
def integrity_checker(filename):
   aws_folder = filename+"_chunks"
   f = open('./record_'+filename+'/manifest','r')
   hashes = eval(f.read())
   f.close()
   s = len(hashes)
   print("total number of available chunks: ",str(s))
   print("================================")
   print("1. Check integrity of all the chunks")
   print("2. Check integrity of any three chunks")
   choice = int(input())
   if choice == 1:
      for i in range(1,s+1):
          filen = "enc-"+filename+"_"+str(i)+".txt"
          download.download_file("enc-files",filen,aws_folder)
          cloud_hash = crc32.generate_hash_for_one(filen)
          if hashes[filen] == cloud_hash:
             print("hash from local storage: "+str(hashes[filen]))
             print("hash of cloud chunk: "+ str(cloud_hash))
             print("hash matched")
             os.system('rm -rf '+filen)
          else:
             print("hash doesn't match for chunk: "+filen)
             print("hash from local storage: "+str(hashes[filen]))
             print("hash of cloud chunk: "+ str(cloud_hash))
   elif choice == 2:
      randomlist = random.sample(range(1, s), 3)
      for i in randomlist:
          filen = "enc-"+filename+"_"+str(i)+".txt"
          download.download_file("enc-files",filen,aws_folder)
          cloud_hash = crc32.generate_hash_for_one(filen)
          if hashes[filen] == cloud_hash:
             print("hash from local storage: "+str(hashes[filen]))
             print("hash of cloud chunk: "+ str(cloud_hash))
             print("hash matched")
             os.system('rm -rf '+filen)
          else:
             print("hash doesn't match for chunk: "+filen)
             print("hash from local storage: "+str(hashes[filen]))
             print("hash of cloud chunk: "+ str(cloud_hash))
      

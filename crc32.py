import zlib
import os


def generating_hashes(filename):
    os.mkdir("record_"+filename)
    hashes=[]
    dir_list=os.listdir('./'+filename+'_chunks')
    no_file=len(dir_list)
    for i in range(no_file):
        with open('./'+filename+'_chunks/'+dir_list[i]) as f:
            content=f.read()
            t=zlib.crc32(bytes(content,'utf-8'))
            hashes.append(t)
            f.close()
    d=dict(zip(dir_list,hashes))
    f=open('./record_'+filename+'/manifest','w')
    f.write(str(d))
    f.close()
    print(d)
    print("Hash generation done!")
    
def generate_hash_for_one(filename):
    f = open(filename,'r')
    content = f.read()
    t = zlib.crc32(bytes(content,'utf-8'))
    return t


from filesplit.split import Split
import os
import base64
def split():
    global inp
    print("Enter the path of a You want to split:")
    inp=input()
    #print("Enter Destination of data chunks :")
    out= 'chunks'
    os.system('mkdir chunks')
    f = open(inp,'r')
    data = f.read()
    #encoded_data = base64.b64encode(data.encode('ascii'))
    f.close()
    f = open('enc-'+inp,'w')
    f.write(str(data))
    f.close()
    try:
        split = Split('enc-'+inp,out).bysize(2090453)
    except:
        print("An Error Occurred During Splitting files")


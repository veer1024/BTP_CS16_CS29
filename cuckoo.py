import cuckoofilter
import os
cf = cuckoofilter.CuckooFilter(capacity=100000, fingerprint_size=1)
if os.path.exists("./hash.txt")==True:
    file1 = open('hash.txt', 'r')
    Lines = file1.readlines()
    for lines in Lines:
        cf.insert(lines)
    file1.close()
else:
    file1 = open('hash.txt', 'w')
    file1.close()
while(True):
    print("Select your Choice : ")
    print("1. Insert a hash in cuckoo filter")
    print("2. Check Weather the hash is present in cuckoo filter or not")
    print("3. Exit the program")
    
    choice=int(input())
    if choice==1:
        print("Enter hash you want to insert :")
        hsh=input()
        try:
            file=open('hash.txt','a')
            file.write(hsh+'\n')
            file.close()
            cf.insert(hsh)
            print("Hash Inserted successfully")
        except:
            print("There is an error occured  during insertion. Try again")
    elif choice==2:
        print("Enter the hash you want to check :")
        hashh=input()
        try:
            if cf.contains(hashh)==True:
                print("Hash present in the Filter")
            else:
                print("Hash not present in the filter. Make sure you Entered correct Hash")
        except:
            print("An error Occured suring checking")
    elif choice==3:
        break
    else:
        print("Invalid Choice")


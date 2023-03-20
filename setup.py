def setup():

    aes_p=input("Enter Passphrase for AES  Encryption : ")
    access_key=input("Enter your AWS  Access Key : ")
    secret_key=input("Enter your AWS Secret Key : ")
    len_aes=len(aes_p)
    while len_aes!=16:
        if len_aes<16:
            aes_p+=aes_p
            len_aes=len(aes_p)
        elif len_aes>16:
            aes_p=aes_p[:16]
            break
        else:
            pass
    AES_Passphrase=aes_p
    res=AES_Passphrase+';'+access_key+';'+secret_key
    f=open('./keys.txt','w')
    f.write(res)
    f.close()
    
setup()

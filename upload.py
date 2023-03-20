import boto3
import creds
from botocore.exceptions import NoCredentialsError
import os
f=open('keys.txt','r')
keys_str=f.read()
keys=keys_str.split(';')
f.close()
ACCESS_KEY = keys[1]
SECRET_KEY = keys[2]


def upload_to_aws(local_folder):
    try:
        #s3.upload_file(local_file, bucket, s3_file)
        #uploadDirectory(local_folder,'enc-files')
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
        for root,dirs,files in os.walk(local_folder):
            for file in files:
                print(file)
                s3.upload_file(os.path.join(root,file),'enc-files',local_folder+'/'+file)

        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


#uploaded = upload_to_aws('local_file', 'bucket_name', 's3_file_name')

def uploadDirectory(path,bucketname):
        s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
        for root,dirs,files in os.walk(path):
            for file in files:
                print(file)
                s3.upload_file(os.path.join(root,file),bucketname,local_folder+'/'+file)


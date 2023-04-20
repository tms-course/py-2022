import boto3

BUCKET_NAME = 'test-bucket-akarpovich'

s3 = boto3.client('s3', 
                  aws_access_key_id='AKIAX43SML5BPTEPLCS6',
                  aws_secret_access_key='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')

buck_res = s3.list_buckets()
for buck in buck_res['Buckets']:
    print(buck)


with open('./test.txt', 'rb') as f:
    s3.upload_fileobj(f, BUCKET_NAME, 'my-file-name.txt')

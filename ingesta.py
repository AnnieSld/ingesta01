import boto3

ficheroUpload = "data.csv"
nombreBucket = "asaldarriaga-students"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, ficheroUpload)
print(response)

print("Ingesta completada")
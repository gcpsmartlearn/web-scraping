import requests

url = "https://storage.googleapis.com/upload/storage/v1/b/odm-sml-bucket/o?uploadType=media&name=image1.png"

payload = "/Users/akshayj/Desktop/1.png"
headers = {
  'Content-Type': 'image/png',
  'Content-Length': '100',
  'Authorization': 'Bearer ya29.a0AfH6SMBAqTYRERMcxTn0wmz5XFLgs68CWMH2SLNfmvY7kYERhNrZ8U78WcwQDH0MJqblsJnd7JiZw-FOKtTpps2_7HK-rk3OLU0pZXSmSW6X7KNoalg4CDWyDjje2Xl2hGxOwvu4ywtLgjpO03nnD6DKxCTW'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

# from google.cloud import storage


# def upload_blob(bucket_name, source_file_name, destination_blob_name):
#     """Uploads a file to the bucket."""
#     # The ID of your GCS bucket
#     # bucket_name = "your-bucket-name"
#     # The path to your file to upload
#     # source_file_name = "local/path/to/file"
#     # The ID of your GCS object
#     # destination_blob_name = "storage-object-name"

#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(destination_blob_name)

#     blob.upload_from_filename(source_file_name)

#     print(
#         "File {} uploaded to {}.".format(
#             source_file_name, destination_blob_name
#         )
#     )
# print(upload_blob("odm-sml-bucket","/Users/akshayj/Desktop/1.png","image22.png"))

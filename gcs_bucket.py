from google.cloud import storage 
import os # Ensure this import is in your file

from google.cloud import storage
def upload_blob(bucket_name, file, destination_blob_name):
    """Uploads a file to the bucket."""
    
    # Initialize the GCS client
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload the file using the file's content
    blob.upload_from_filename(file)

    print(f"File {file} uploaded to {destination_blob_name}.")
# def upload_to_gcs(file_data, file_name):
#     # Create a client
#     client = storage.Client(project='sinuous-faculty-434016-n4')
#     bucket_name = 'chainlit_rag-bucket'

#     # Get the bucket
#     bucket = client.get_bucket(bucket_name)

#     # Create a new blob (object) in the bucket
#     blob = bucket.blob(file_name)

#     # Upload the file to GCS
#     blob.upload_from_string(file_data)

#     # Generate the GCS file URL
#     file_url = f"gs://{bucket_name}/{file_name}"
    
#     print(f"File {file_name} uploaded to {file_url}.")

#     # Return the GCS file URL
#     return file_url



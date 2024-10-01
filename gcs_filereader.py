import gcsfs
from pypdf import PdfReader
from urllib.parse import urlparse


from langchain_google_community import GCSFileLoader

# loader = GCSFileLoader(project_name="sinuous-faculty-434016-n4", bucket="chainlit_rag-bucket", blob="Tech-Report-Generative-AI-.pdf")

# loader.load()
from langchain_community.document_loaders import PyPDFLoader


def load_pdf(file_path):
    return PyPDFLoader(file_path)


loader = GCSFileLoader(project_name="sinuous-faculty-434016-n4", bucket="chainlit_rag-bucket", blob="Tech-Report-Generative-AI-.pdf", loader_func=load_pdf)
pages = loader.load_and_split()
pages[0]
print(pages[0])

# def _download_from_google_bucket(self, url: str) -> str:
#         # """Download a file from a Google bucket to a temporary file."""
#         parsed = urlparse(url)
#         bucket_name = parsed.netloc
#         blob_name = parsed.path.lstrip('/')
#         _, suffix = os.path.splitext(blob_name)
#         temp_pdf = os.path.join(self.temp_dir.name, f"tmp{suffix}")

#         storage_client = storage.Client()
#         bucket = storage_client.bucket(bucket_name)
#         blob = bucket.blob(blob_name)
#         blob.download_to_filename(temp_pdf)

#         return temp_pdf

# gcs_file_system = gcsfs.GCSFileSystem(project="sinuous-faculty-434016-n4")
# gcs_pdf_path = "gs://chainlit_rag-bucket/Tech-Report-Generative-AI-.pdf"

# f_object = gcs_file_system.open(gcs_pdf_path, "rb")
# print(f_object)
    
# Open our PDF file with the PdfReader
#reader = PdfReader(f_object)
  
# Get number of pages
#num = len(reader.pages)

#f_object.close()

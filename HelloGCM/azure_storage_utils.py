from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from django.conf import settings

def upload_to_azure_blob(file, container_name, blob_name):
    try:
        # Create a BlobServiceClient
        blob_service_client = BlobServiceClient(account_url=f"https://{settings.AZURE_ACCOUNT_NAME}.blob.core.windows.net/",
                                               credential=settings.AZURE_ACCOUNT_KEY)

        # Get or create a container
        container_client = blob_service_client.get_container_client(container_name)
        if not container_client.exists():
            container_client.create_container()

        # Upload file to Azure Blob Storage
        blob_client = container_client.get_blob_client(blob_name)
        with open(file, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        # Get the URL of the uploaded file
        blob_url = blob_client.url
        return blob_url

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

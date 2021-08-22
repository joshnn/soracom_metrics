from flask import Flask
import dotenv
from dotenv import load_dotenv
from google.cloud import storage
import csv
import datetime

load_dotenv()

app = Flask(__name__)


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    return blobs

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The ID of your GCS object
    # source_blob_name = "storage-object-name"

    # The path to which the file should be downloaded
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Downloaded storage object {} from bucket {} to local file {}.".format(
            source_blob_name, bucket_name, destination_file_name
        )
    )

@app.route("/")
def index():
    storage_client = storage.Client()

    res = ""

    bucket_name = "soracomalarms"
    res += "<table border=1>\n"
    res += "<th><td>source</td><td>dest</td><td>latency</td></th>\n"

    for blob in list_blobs(bucket_name):
        local_name = '/tmp/' + blob.name
        download_blob(bucket_name, blob.name, local_name)
        with open(local_name) as f:
            reader = csv.DictReader(f)
            for l in reader:
                res += '<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td><tr>\n'.format(
                    l["timestamp"],
                    l['source'],
                    l["target"],
                    l["latency"]
                    )

    res += "</table>\n"
    return res


import os
import subprocess

WORKING_DIR = os.getcwd()

def download_files_from_gcs(source, destination):
    local_file_names = [destination]
    gcs_input_paths = [source]

    # Copy raw files from GCS into local path.
    raw_local_files_data_paths = [os.path.join(WORKING_DIR, local_file_name)
        for local_file_name in local_file_names
        ]
    
    for i, gcs_input_path in enumerate(gcs_input_paths):
        if gcs_input_path:
            subprocess.check_call(
                ['gsutil', 'cp', gcs_input_path, raw_local_files_data_paths[i]])

    return raw_local_files_data_paths

# https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python

# https://cloud.google.com/storage/docs/downloading-objects#code-samples


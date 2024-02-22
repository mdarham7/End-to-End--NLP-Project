from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.gcloud_syncer import GCloudSync
import sys

logging.info("Welcome to my Project")

obj = GCloudSync()
obj.sync_folder_from_gcloud("hate_speechproject","dataset.zip", "download/dataset.zip")
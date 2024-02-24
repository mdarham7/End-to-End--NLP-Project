import os
import sys
from zipfile import ZipFile
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.s3_operations import S3Operation
from hate.entity.config_entity import DataIngestionConfig
from hate.entity.artifact_entity import DataIngestionArtifacts


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config

        self.s3 = S3Operation()

    def get_data_from_s3(self) -> None:
        try:
            logging.info("Entered the get_data_from_s3 method of Data ingestion class")

            self.s3.sync_folder_from_s3(
                folder=self.data_ingestion_config.data_path,
                bucket_name=self.data_ingestion_config.bucket_name,
                bucket_folder_name=self.data_ingestion_config.s3_data_folder,
            )

            logging.info("Exited the get_data_from_s3 method of Data ingestion class")

        except Exception as e:
            raise CustomException(e, sys)
        
        

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        logging.info(
            "Entered the initiate_data_ingestion method of Data ingestion class"
        )

        try:
            self.get_data_from_s3()

            data_ingestion_artifacts = DataIngestionArtifacts(
                imbalanced_data_file_path=self.data_ingestion_config.imbalanced_data_file_path,
                raw_data_file_path=self.data_ingestion_config.raw_data_file_path,
            )

            logging.info(
                "Exited the initiate_data_ingestion method of Data ingestion class"
            )

            return data_ingestion_artifacts

        except Exception as e:
            raise CustomException(e, sys)
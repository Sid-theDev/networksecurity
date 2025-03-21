from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_validation import DataValidation
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys
from networksecurity.components.data_transformation import DataTransformation

if __name__ == "__main__":
    try:
        training_pipeline_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeline_config)
        data_ingestion = DataIngestion(data_ingestion_config)
        logging.info("Initiatiing of Data Ingestion")
        data_ingestion_artificat = data_ingestion.initiate_data_ingestion()
        logging.info("Data Ingestion Completed")
        print(data_ingestion_artificat)
        data_validation_config = DataValidationConfig(training_pipeline_config)
        data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artificat, data_validation_config=data_validation_config)
        logging.info("Initiate the data validation")
        data_validation_artificat = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(data_validation_artificat)

        data_transformation_config = DataTransformationConfig(training_pipeline_config)
        logging.info("Data Transformation Started")
        data_transformation = DataTransformation(data_validation_artificat, data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("Data Transformation Completed")

    except Exception as e:
        raise NetworkSecurityException(e, sys)

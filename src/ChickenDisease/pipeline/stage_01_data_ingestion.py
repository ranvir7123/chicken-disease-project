from src.ChickenDisease.config.configuration import ConfigurationManager
from src.ChickenDisease.components.data_ingestion import DataIngestion
from src.ChickenDisease import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
            logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")
        except Exception as e:
            logger.error(f"Error in {STAGE_NAME}: {e}")
            raise e

if __name__ == '__main__':
    pipeline = DataIngestionTrainingPipeline()
    pipeline.main()
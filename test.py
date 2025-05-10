import ProdPipeline

from src.ProdPipeline import logger

logger.info("Welcome to our custom logging")
logger.info("This is an info message")
logger.info("Path to the files")

for i in range(5):
    logger.info(f"Logging message {i+1}")
from PredictionModel.logger import logging
from PredictionModel.exception import CustomException 
import os,sys


def test_logger_and_exception():
    try:
        logging.info("Starting the Test Logger and Exception ")
        result = 3/0
        print(result)
        logging.info("Ending Point of the Test Logger and Exception ")
        
    except Exception as e:
        logging.debug(str(e))
        raise CustomException(e,sys)   # e is exception and sys is the model to be define 
    
    if  __name__ == "__main__":
        try:
            test_logger_and_exception()
        except Exception as e:
            print(e)
    
        
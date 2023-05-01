import pandas as pd
import numpy as np 
import os
import sys
from PredictionModel.exception import CustomException 
from PredictionModel.config import mongo_client
from PredictionModel.logger import logging


def get_collection_as_dataframe(database_name:str,collection_name:str):
    try:
        logging.ino(f"Reading Data from : {database_name} and collection {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())  # this snippet will find database name and collection name from mongodb client server
        logging.info(f"Find columns : {df.columns} ")
        if "_id" in df.columns:
            logging.info(f"Dropping Columns: _id ")
            df = df.drop("_id",axis =1)
        logging.info(f"Rows and Columns in df : {df.shape} ")
        return df 
    
    
    
    except Exception as e:
        raise CustomException(e,sys)    
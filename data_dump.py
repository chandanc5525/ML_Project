import pymongo
import pandas as pd
import json 
from pymongo.mongo_client import MongoClient


# Create a new client and connect to the server
client = pymongo.MongoClient("mongodb+srv://MachineLearning:ganesh22@atlascluster.nu0ydew.mongodb.net/?retryWrites=true&w=majority")
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
DATA_FILE_PATH = (r"E:\ML_Project\Data_Cortex_Nuclear.csv")
DATA_BASE = "MICE_PROTEIN_PREDICTION"
COLLECTION_NAME = "PREDICTION_MODEL"

if __name__ == "__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and Columns : {df.shape} ")
    df.reset_index(drop = True , inplace=True)
    
    # Note:- As Mongodb Takes Data Into Keys and Value So Need to Transpose the Data
    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    # To Insert All The Dataset Values into the Mongodb Cloud 
    client[DATA_BASE][COLLECTION_NAME].insert_many(json_record)
    
import awswrangler as wr
import pandas as pd
import os
from joblib import dump, load
import boto3

boto3.setup_default_session(region_name="us-east-2")

BUCKET_NAME = 'team4-guai-artificial-intelligence-685653615554'
ROOT_BUCKET_PATH = f's3://{BUCKET_NAME}/'
INTERMEDIATE_FOLDER_NAME = '02_intermediate'
INTERMEDIATE_FOLDER_PATH = os.path.join(ROOT_BUCKET_PATH, INTERMEDIATE_FOLDER_NAME)
MODELS_FOLDER_NAME = '06_models'
MODELS_FOLDER_PATH = os.path.join(ROOT_BUCKET_PATH, MODELS_FOLDER_NAME)

def read_table_to_pandas(database: str, table: str, format: str='parquet'):
    """
    Read a existing table in catalog to a pandas dataframe.
    It gets the table path using the catalog.

    Inputs:
        database: string with the name of existing catalog database
        table: string with the name of existing catalog table
        format: str with format of table file located in s3 path
    """

    path = wr.catalog.get_table_location(database=database, table=table)
    if format=='parquet':
        return wr.s3.read_parquet(path=path)
    elif format=='csv':
        return wr.s3.read_csv(path=path)

    raise Exception("El archivo que intenta cargar no está en formato parquet o csv")

def save_dataframe_to_s3_parquet(dataframe: pd.DataFrame, path: str, database: str, table: str):
    """
    Save a pandas dataframe to a parquet file in a s3 path.
    If table in catalog already exists in the same path it is replaced

    Inputs:
        dataframe: pandas dataframe to be saved
        path: string containing s3 path
        database: string with name of existing database in catalog
        table: string with the existing o new name of a table to be created in catalog

    Returns:
        None
    """

    wr.s3.to_parquet(
        df=dataframe,
        path=path,
        compression='snappy',
        database=database,
        table=table,
        dataset=True
    )

def save_model_to_s3(model, model_name):
    """
    Takes a pre-train sklean model and saves it into the "models" folder of the s3 bucket.
    To do that it has to save to sagemaker local host the file, send it to s3, and delete it from sagemaker

    Inputs:
        model: sklearn model to be saved
        model_name: a user assign name for the model MUST END WITH "".joblib" sufix

    Returns:
        None

    """
    dump(model, model_name)
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(model_name, BUCKET_NAME, os.path.join(MODELS_FOLDER_NAME, model_name))
    os.remove(model_name)

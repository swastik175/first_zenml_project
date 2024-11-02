import logging
import pandas as pd
from zenml import step

class Ingestdata:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def get_data(self):
            logging.info(f"Ingesting data  from {self.data_path}")
            return pd.read_csv(self.data_path)

@step
def ingest_df(data_path: str) -> pd.DataFrame:

    """
    Ingesting Data from the data path
    Args is data_path: path to the data present in the .csv
    Returns pd as a Dataframe as the ingested data
    """

    try:
        ingest_data = Ingestdata(data_path)
        df = ingest_data.get_data()
        return df
    except Exception as e:
        logging.error("Error caused due to {e}")
        raise e
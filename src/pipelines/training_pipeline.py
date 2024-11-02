from zenml import pipeline
from steps.ingest_data import ingest_df
from steps.clean_data import clean_data
from steps.train_model import train_model
from steps.evaluate import evaluate

@pipeline
def train_pipeline(data_path: str):
    df = ingest_df(data_path)
    clean_data(df)
    train_model(df)
    evaluate(df)
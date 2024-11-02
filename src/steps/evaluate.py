import logging
from zenml import step
import pandas as pd
@step
def evaluate(df: pd.DataFrame) -> None:
    pass
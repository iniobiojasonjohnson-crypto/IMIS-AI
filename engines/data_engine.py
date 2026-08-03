import pandas as pd
from pathlib import Path

class DataEngine:

    def __init__(self):

        self.data_folder = Path("data")

        self.data_folder.mkdir(exist_ok=True)

    def load_csv(self,file):

        df = pd.read_csv(file)

        return df

    def save_parquet(self,df,name):

        file = self.data_folder / f"{name}.parquet"

        df.to_parquet(file,index=False)

    def read_parquet(self,name):

        file = self.data_folder / f"{name}.parquet"

        return pd.read_parquet(file)

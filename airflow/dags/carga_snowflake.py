import os
import pandas as pd
import numpy as np
import kagglehub
from sqlalchemy import create_engine
from snowflake.connector.pandas_tools import write_pandas
from datetime import datetime
from urllib.parse import quote_plus

USER = 'gyamada22'
RAW_PASS = '@Guigabia12345' 
PASSWORD = quote_plus(RAW_PASS)
ACCOUNT = 'KDBKQEA-GK51114' 
DATABASE = 'FINANCE_DB'
SCHEMA = 'BRONZE'
WAREHOUSE = 'COMPUTE_WH'

os.environ["KAGGLE_API_TOKEN"] = "KGAT_0fd375570be5aa87bac89a00f7fba5ac"

def executar_pipeline():
    path = kagglehub.dataset_download("mathchi/churn-for-bank-customers")
    csv_file = [f for f in os.listdir(path) if f.endswith('.csv')][0]
    df = pd.read_csv(os.path.join(path, csv_file))
    
    df.columns = [c.upper().replace(' ', '_').strip() for c in df.columns]
    
    if 'ROWNUMBER' in df.columns:
        df = df.drop(columns=['ROWNUMBER'])
    
    df['DATA_CARGA'] = datetime.now()
    df = df.replace({np.nan: None})
    
    url = f'snowflake://{USER}:{PASSWORD}@{ACCOUNT}/{DATABASE}/{SCHEMA}?warehouse={WAREHOUSE}'
    engine = create_engine(url)
    
    with engine.connect() as conn:
        success, _, nrows, _ = write_pandas(
            conn=conn.connection,
            df=df,
            table_name='RAW_BANK_CHURN',
            database=DATABASE,
            schema=SCHEMA,
            auto_create_table=True,
            overwrite=True,
            quote_identifiers=False
        )
    
    if success:
        print(f"{nrows} linhas enviadas com sucesso!")

if __name__ == "__main__":
    executar_pipeline()
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import kagglehub

def ingestao_task():
    path = kagglehub.dataset_download("mathchi/churn-for-bank-customers")
    print(f"Dados baixados em: {path}")

with DAG(
    dag_id='ingestao_snowflake_bronze_v1',
    start_date=datetime(2026, 1, 1),
    schedule_interval='@daily',
    catchup=False
) as dag:

    task_carga = PythonOperator(
        task_id='carga_kaggle_para_bronze',
        python_callable=ingestao_task
    )
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import sys

sys.path.append('/opt/airflow/dags')
from carga_snowflake import executar_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'pipeline_churn_bancario_end_to_end',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
) as dag:

    task_ingestao_python = PythonOperator(
        task_id='ingestao_kaggle_para_snowflake',
        python_callable=executar_pipeline
    )

    task_transformacao_dbt = BashOperator(
        task_id='transformacao_dbt_silver',
        bash_command='cd /opt/airflow/dbt_churn && dbt run --profiles-dir .'
    )

    task_ingestao_python >> task_transformacao_dbt
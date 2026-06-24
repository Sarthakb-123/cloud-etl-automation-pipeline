from airflow import DAG
from airflow.operators.python import (
    PythonOperator
)

from datetime import datetime

from scripts.main import (
    run_pipeline
)

with DAG(
    dag_id="cloud_etl_pipeline",
    start_date=datetime(
        2025,
        1,
        1
    ),
    schedule="@daily",
    catchup=False
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_pipeline
    )

    etl_task
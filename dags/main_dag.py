import os
from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

def task_s3_log_load():
    hook = S3Hook(aws_conn_id='aws_default')

    # Get list of objects on a bucket
    keys = hook.list_keys('jungwoohan-temp-source-bucket')

    for key in keys:
        print(key)

        obj = hook.get_key(key, 'jungwoohan-temp-source-bucket')

        print(obj.bucket_name, obj.key)

with DAG(
    dag_id='main',
    schedule_interval='@daily',
    start_date=datetime(2022, 3, 1),
    catchup=False
) as dag:
    task_1 = PythonOperator(
        task_id='s3_analysis',
        python_callable=task_s3_log_load,
        dag=dag
    )

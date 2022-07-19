import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG(
    dag_id="jungwoohan_hihi",
    schedule_interval=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
) as dag:

    def print_array():
        """Print Numpy array."""
        # import numpy as np  # <- THIS IS HOW NUMPY SHOULD BE IMPORTED IN THIS CASE
        a = ['hello hsjfdsjdlfl sdkjflksdjfkskfs sdkjfkls hanjungwoo hanjungwoo lgcns']
        # a = np.arange(15).reshape(3, 5)
        print(a)
        return a

    run_this = PythonOperator(
        task_id="print_the_context",
        python_callable=print_array,
    )

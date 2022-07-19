from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args={
    'owner': 'airflow',
}

dag = DAG(
    "jungwoohan_dag",
    description='My first tutorial bash DAG',
    default_args=default_args,
)

t1 = BashOperator(
    task_id='say_hello',
    bash_command='echo "hello world"',
    dag=dag
)

t2 = BashOperator(
    task_id='what_time',
    bash_command='date',
    dag=dag
)

t1 >> t2
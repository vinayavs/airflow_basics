from airflow import DAG
from airflow.operators.bash import BashOperator
from groups.downloads_group import download_tasks
from groups.transfrom_group import transform_tasks


from datetime import datetime

with DAG(
    dag_id='task_group_dag',
    start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily',
    catchup=False
) as dag:
    


    downloads=download_tasks()

    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    
    transform=transform_tasks()

    downloads >> check_files >> transform
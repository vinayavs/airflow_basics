from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.subdag import SubDagOperator
from subdags.downloads_subdag import downloads_subdag
from subdags.transfrom_subdag import transform_subdag


from datetime import datetime

with DAG(
    dag_id='group_dag',
    start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily',
    catchup=False
) as dag:
    
    args={
        "start_date":dag.start_date,
        "schedule_interval":dag.schedule_interval,
        "catchup":dag.catchup
    }

    downloads=SubDagOperator(
        task_id="downloads",
        subdag=downloads_subdag(dag.dag_id, "downloads", args)
    )

    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )
    
    transform=SubDagOperator(
        task_id="transfrom",
        subdag=transform_subdag(dag.dag_id, "transfrom", args)
    )

    downloads >> check_files >> transform
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from test_python_transformation import test_clean_amount,test_clean_Date


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 28),
    'retries': 1,
    'retry_delay': timedelta(seconds=2),
}

with DAG('Unit_Test_Dag', default_args=default_args, schedule_interval=timedelta(days=1), catchup=False) as dag:
    
    # Task 2 : transformation et création du nouveau fichier
    t1 = PythonOperator(
        task_id='UnitTestAmount',
        python_callable=test_clean_amount,
    )

     # Task 4 : création de la table Postgres
    t2 = PythonOperator(
        task_id='UnitTestCleanDate',
        python_callable=test_clean_Date,
    )

    # Les deux tâches seront faîtes simultanéments
    [t1,t2] 

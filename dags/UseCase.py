import os
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from postgres_commands import create_table, insert_data_from_csv
from python_Transformation_file import stats_Bookings


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 28),
    'retries': 1,
    'retry_delay': timedelta(seconds=2),
}

with DAG('Use_Case_Dag', default_args=default_args, schedule_interval=timedelta(days=1), catchup=False) as dag:
    
    # Task 1 : vérification de l'existence du fichier
    t1 = BashOperator(
        task_id='check_file',
        bash_command='shasum ~/csvFile/bookings.csv',
        retries=1,
    )

    # Task 2 : transformation et création du nouveau fichier
    t2 = PythonOperator(
        task_id='Stats_Bookings_Csv',
        python_callable=stats_Bookings,
    )

    # Task 3 : vérification de l'existence du nouveau fichier
    t3 = BashOperator(
        task_id='check_new_file',
        bash_command='shasum ~/csvFile/monthly_restaurants_report.csv',
        retries=1,
    )
    
    # Task 4 : création de la table Postgres
    t4 = PythonOperator(
        task_id='Create_table',
        python_callable=create_table,
    )

    # Task 5 : insertion des données dans la nouvelle table Postgres
    t5 = PythonOperator(
        task_id='insert_data_from_csv',
        python_callable=insert_data_from_csv,
        op_args=[os.path.expanduser("~/csvFile/monthly_restaurants_report.csv")],
    )

    # Chaque tâches doit attendre que la précédente se termine
    t1 >> t2 >> t3 >> t4 >> t5

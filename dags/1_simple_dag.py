from airflow.decorators import task, dag
from datetime import datetime


@dag(
    schedule=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
    dag_id="simple"
)
def simple():
    @task
    def return_goodbye_message():
        message = "May the force be with you!"
        print(message)
        return message

    return_goodbye_message()

dag = simple()

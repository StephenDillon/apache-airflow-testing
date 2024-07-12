from airflow.decorators import task, dag
from datetime import datetime, timedelta


@dag(
    schedule=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
    default_args={
        "start_date": datetime(2022, 1, 1),
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    dag_id="simple",
    tags=["1_simple_dag"],
)
def simple():
    @task
    def return_goodbye_message():
        message = "May the force be with you!"
        print(message)
        return message

    return_goodbye_message()

dag = simple()

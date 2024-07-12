from airflow.decorators import task, dag
from datetime import datetime, timedelta
import requests


@dag(
    schedule=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
    default_args={
        "start_date": datetime(2022, 1, 1),
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    dag_id="http_dag",
    tags=["2_http_dag"],
)
def http_dag():
    @task
    def fetch_json_from_github():
        url = "https://raw.githubusercontent.com/StephenDillon/apache-airflow-testing/main/starwars.json"
        response = requests.get(url)
        data = response.json()
        return data

    @task
    def sort_characters_by_lightsaber_color(data):
        sorted_data = sorted(data, key=lambda x: (x["lightsaberColor"], x["name"]))
        return sorted_data

    @task
    def identify_sith_characters(data):
        for character in data:
            if character["type"] == "Sith":
                character["alignment"] = "Sith"
            else:
                character["alignment"] = "Not Sith"
        return data

    fetch = fetch_json_from_github()
    sort_characters_by_lightsaber_color(fetch)
    identify_sith_characters(fetch)


dag = http_dag()

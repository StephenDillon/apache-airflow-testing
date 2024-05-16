from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta
import requests


@task(task_id="fetch_json")
def fetch_json_from_github():
    url = (
        "https://raw.githubusercontent.com/your_username/your_repository/main/data.json"
    )
    response = requests.get(url)
    data = response.json()
    return data


@task(task_id="sort_characters")
def sort_characters_by_lightsaber_color(data):
    sorted_data = sorted(data, key=lambda x: (x["lightsaber_color"], x["name"]))
    return sorted_data


@task(task_id="identify_sith")
def identify_sith_characters(data):
    for character in data:
        if character["is_sith"]:
            character["alignment"] = "Sith"
        else:
            character["alignment"] = "Not Sith"
    return data


default_args = {
    "owner": "your_name",
    "start_date": datetime(2022, 1, 1),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG("starwars_dag", default_args=default_args, schedule_interval="@daily") as dag:
    fetch_json_from_github >> [
        sort_characters_by_lightsaber_color,
        identify_sith_characters,
    ]

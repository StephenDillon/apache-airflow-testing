from airflow.decorators import task, dag
from airflow.providers.http.hooks.http import HttpHook
from datetime import datetime

@dag(
    schedule=None,
    start_date=datetime(2022, 1, 1),
    catchup=False,
    dag_id="http"
)
def http_dag():
    @task
    def fetch_json():
        http_get = HttpHook(method="GET", http_conn_id="data_api")
        return http_get.run(endpoint="starwars.json").json()

    @task
    def sort_characters_by_lightsaber_color(data):
        sorted_data = sorted(data, key=lambda x: (x["lightsaberColor"], x["name"]))
        return sorted_data

    @task
    def get_sith_characters(data):
        sith_names = [character["name"] for character in data if character["type"] == "Sith"]
        print(sith_names)
        return sith_names

    fetch = fetch_json()
    sort_characters_by_lightsaber_color(fetch)
    get_sith_characters(fetch)


dag = http_dag()

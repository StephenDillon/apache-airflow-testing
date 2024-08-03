import pytest
from airflow import settings
from airflow.models import DagBag
from airflow.models.connection import Connection
from airflow.models.dag import DAG


# This will test the DAG is valid and the tasks are properly set up
def get_dag(dag_bag: DagBag, dag_id: str) -> DAG:
    dag = dag_bag.get_dag(dag_id)
    assert dag is not None
    return dag


# Returns the result of the task execution
def get_result(results, task_id):
    ti = results.get_task_instance(task_id=task_id)
    return ti.xcom_pull(task_ids=task_id, key="return_value")


@pytest.fixture(scope="session")
def dag_bag() -> DagBag:
    dag_bag = DagBag(include_examples=False, dag_folder="dags")
    assert dag_bag.import_errors == {}
    return dag_bag


@pytest.fixture(scope="session")
def httpserver_listen_address():
    return ("127.0.0.1", 8000)


def stub_http_request(httpserver, endpoint, response):
    httpserver.expect_request(endpoint).respond_with_json(response)


# Here we setup stub connections for airflow
@pytest.fixture(scope="session", autouse=True)
def setup_module():
    session = settings.Session()
    clean_connections(session)

    data_api = Connection(
        conn_id="data_api",
        conn_type="http",
        host="http://127.0.0.1:8000/",
    )
    session.add(data_api)
    session.commit()


# Avoid issues caching connections, we clean the connections before each test
def clean_connections(session):
    existing_connections = (
        session.query(Connection).filter(Connection.conn_id == "data_api").all()
    )
    for connection in existing_connections:
        session.delete(connection)
    session.commit()

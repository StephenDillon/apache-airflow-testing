# apache-airflow-testing
Demo project showing how to test apache airflow DAGs

### Prerequisites
Install the following:
- Python
- Poetry
- Docker

### Setup
1. Run `poetry shell` to activate the virtual environment
2. Run `poetry install` to install the dependencies

### Optional: Run Apache Airflow Locally
You can run Apache Airflow locally using docker if you want, but it will not be required to run the tests. Follow https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

### Running the Tests
`pytest` to run the tests
`pytest -v -s` for verbose output and to see print statements
`pytest -k <test_name>` to run a specific test
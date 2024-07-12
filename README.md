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
3. Apache Airflow doesnt support installation via Poetry, so you also need to follow install instructions from https://airflow.apache.org/docs/apache-airflow/stable/installation/installing-from-pypi.html .`pip install apache-airflow` worked for me to install it

### Run Apache Airflow Locally
You can run Apache Airflow locally by following the instructions from https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html
I have included a `docker-compose.yaml` I use with a very simple setup. You can run it by running `docker-compose up` in the root directory of this project

### Running the Tests
`pytest` to run the tests
`pytest -v -s` for verbose output and to see print statements
`pytest -k <test_name>` to run a specific test
from .conftest import get_dag, get_result

# This will execute the DAG tasks and test the return value of the task
def test_return_goodbye_message(dag_bag):
    dag = get_dag(dag_bag, "simple")

    results = dag.test()  # execute the DAG and get the DagRun response
    assert get_result(results, "return_goodbye_message") == "May the force be with you!"
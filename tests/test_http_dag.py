from tests.conftest import get_dag, get_result, stub_http_request


def test_http_dag(dag_bag, httpserver):
    dag = get_dag(dag_bag, "http")
    response_data = [
        {"name": "Darth Vader", "lightsaberColor": "red", "type": "Sith"},
        {"name": "Darth Maul", "lightsaberColor": "red", "type": "Sith"},
        {"name": "Obi-Wan Kenobi", "lightsaberColor": "blue", "type": "Jedi"},
    ]
    stub_http_request(
        httpserver,
        "/starwars.json",
        response_data,
    )

    results = dag.test()  # execute the DAG and get the DagRun response
    assert get_result(results, "get_sith_characters") == ['Darth Vader', 'Darth Maul']

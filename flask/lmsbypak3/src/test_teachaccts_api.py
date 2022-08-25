import requests

def test_get_teachaccts_check_status_code_equals_200():
    response = requests.get("http://127.0.0.1:5000/teachaccts")
    assert response.status_code == 200
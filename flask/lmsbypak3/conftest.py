#from src import create_app
import pytest

@pytest.fixture
def new_teachaccts():
    new_user = {
        'username': 'jjackson',
        'password': 'JJ123'
    }
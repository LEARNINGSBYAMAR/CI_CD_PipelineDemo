import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_login_page_load(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login Page' in response.data


def test_valid_login(client):
    response = client.post('/', data={
        'username': 'admin',
        'password': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome to Dashboard! hooo' in response.data


def test_invalid_login(client):
    response = client.post('/', data={
        'username': 'wrong',
        'password': 'wrong'
    })
    assert response.status_code == 401

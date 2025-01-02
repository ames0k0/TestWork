from fastapi.testclient import TestClient

from restapi.app import app
from restapi import connections


connections.Postgres.initialize()
connections.Redis.initialize()
connections.Celery.initialize()

HEADERS = {
    "ApiKey": "TestWork005",
}

client = TestClient(app)


def test_header_api_key_required():
    response = client.post('/transactions').json()
    assert response['detail'][0]['type'] == 'missing'
    assert 'ApiKey' in response['detail'][0]['loc']


def test_post_transactions():
    response = client.post(
        "/transactions",
        headers=HEADERS,
        json={
            "transaction_id": "1",
            "user_id": 1,
            "amount": 1,
            "currency": "RUS",
            "timestamp": "2024-12-12T12:00:00"
        }
    ).json()
    assert response['message'] == 'Transaction received'


def test_get_statistics():
    # NOTE: added 1 transaction,
    # for the large data we may need to wait tasks to be finished
    response = client.get(
        "/statistics",
        headers=HEADERS,
    ).json()
    # default is '0',
    # even if there is no transactions for this ApiKey
    assert response['total_transactions'] > 0


def test_delete_transactions():
    response = client.delete(
        "/transactions",
        headers=HEADERS,
    )
    assert response.status_code == 200

    response = client.get(
        "/statistics",
        headers=HEADERS,
    ).json()
    assert response['total_transactions'] == 0

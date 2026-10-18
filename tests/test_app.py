import pytest

from app.main import create_app


@pytest.fixture()
def client():
    app = create_app()
    app.config.update(TESTING=True)
    return app.test_client()


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Woodpecker" in res.get_json()["message"]


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_add_ok(client):
    res = client.get("/add?a=2&b=3.5")
    assert res.status_code == 200
    assert res.get_json()["result"] == 5.5


@pytest.mark.parametrize("query", ["", "?a=1", "?a=x&b=2"])
def test_add_bad_input(client, query):
    res = client.get("/add" + query)
    assert res.status_code == 400

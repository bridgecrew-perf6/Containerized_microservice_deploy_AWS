from main import translate, app
import pytest


@pytest.fixture()
def client(app):
    return app.test_client()


def test_translattion():
    text = "一个人"
    assert translate(text) == "Alone."


def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_translate(client):
    response = client.get("/translate")
    assert response.status_code == 200


def test_tell_story(client):
    response = client.get("/tell_story")
    assert response.status_code == 200

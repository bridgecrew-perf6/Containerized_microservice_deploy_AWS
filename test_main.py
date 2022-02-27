from main import translate, app

def test_translation():
    text = "一个人"
    assert translate(text) == "Alone."


def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200


def test_translate():
    response = app.test_client().get("/translate")
    assert response.status_code == 200


def test_tell_story():
    response = app.test_client().get("/tell_story")
    assert response.status_code == 200

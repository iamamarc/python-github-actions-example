from application import app


def test_app_index():
    assert app.index() == "Hello World!"

from operator import is_not


def test_is_healthy(app):
    assert app.is_healthy()


def test_greet(app):
    app.greet("e2e_bot", "hi there from greeter bot")


def test_login_valid_user(app):
    response_body = app.login("admin", "password")
    is_not(response_body["access_token"], None)

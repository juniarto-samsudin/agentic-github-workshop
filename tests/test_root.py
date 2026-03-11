def test_root_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200


def test_root_returns_welcome_message(client):
    response = client.get("/")
    assert response.json()["message"] == "Welcome to the Todo API"


def test_root_returns_docs_path(client):
    response = client.get("/")
    assert response.json()["docs"] == "/docs"

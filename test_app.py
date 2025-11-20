import requests
def test_root_response():
    # start app separately during CI or use client in more advanced tests;
    # here we do a simple smoke test using Flask's test client instead:
    from app import app
    client = app.test_client()
    rv = client.get('/')
    assert rv.status_code == 200
    assert b"Hello from Jenkins + Docker CI/CD!" in rv.data

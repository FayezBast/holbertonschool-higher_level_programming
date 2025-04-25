import requests

BASE_URL = "http://127.0.0.1:8000"

def test_root():
    r = requests.get(BASE_URL + "/")
    assert r.status_code == 200
    assert r.text == "Hello, this is a simple API!"
    print("Test if root endpoint returns correct content.: OK")

def test_data():
    r = requests.get(BASE_URL + "/data")
    assert r.status_code == 200
    data = r.json()
    assert data == {"name": "John", "age": 30, "city": "New York"}
    print("Test if data endpoint returns correct data.: OK")

def test_status():
    r = requests.get(BASE_URL + "/status")
    assert r.status_code == 200
    assert r.text == "OK"
    print("Test if status endpoint returns correct status.: OK")

def test_undefined():
    r = requests.get(BASE_URL + "/undefined")
    assert r.status_code == 404
    assert r.json() == {"error": "Endpoint not found"}
    print("Test if undefined endpoint returns correct status.: OK")

if __name__ == "__main__":
    test_root()
    test_data()
    test_status()
    test_undefined()

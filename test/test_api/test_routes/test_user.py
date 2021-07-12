from fastapi.testclient import TestClient

from app.main import app

#app = FastAPI()
client = TestClient(app)

# def test_get_users():
#     response = client.get("http:localhost:5000/api/users")
#     print('123', response.json())
#     print('456', response.status_code)
#     assert response.status_code == 200
#     assert response.json() == [{'user1':'content1'}, {'user2':'content2'}]

@app.get("/")
def read_main():
    return {"msg": "Hello World"};

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
from server import app
import json     
with app.app.test_client() as c:
    response = c.get('/api/people/Farrell')
    data = json.loads(response.data)
    assert data["fname"] == "Doug"
    assert response.status_code == 200

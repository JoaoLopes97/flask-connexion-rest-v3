from server import app
with app.test_client() as c:
    response = c.get('/api/people/Farrell')
    assert response.data.fname == b'Doug'
    assert response.status_code == 200

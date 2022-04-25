import app

def test_home_page(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def test_about_page(app, client):
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200

def test_estimate_page(app, client):
    with app.test_client() as test_client:
        res = test_client.get('estimate')
        assert res.status_code == 200


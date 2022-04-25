import app

def Test_home_page():
    with app.test_client() as test_client:
        res = test_client.get('/')
        assert res.status_code == 200

def Test_about_page():
    with app.test_client() as test_client:
        res = test_client.get('/about')
        assert res.status_code == 200

def Test_estimate_page():
    with app.test_client() as test_client:
        res = test_client.get('estimate')
        assert res.status_code == 200


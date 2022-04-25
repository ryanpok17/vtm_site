import app

def test_maintanace_cost(app, client):
    with app.test_client() as test_client:
        radius = 180
        height = 360
        res = test_client.post('/estimate', data=radius,height)
        assert res.status_code == 302 # Found
    
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert app.estimate == 141,300.00
    
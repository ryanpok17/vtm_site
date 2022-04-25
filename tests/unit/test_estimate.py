import app

def test_maintanace_cost(app, client):
    with app.test_client() as test_client:
        tank = {"radius":180, "height":360}
        res = test_client.post('/estimate', data=tank)
        assert res.status_code == 400 # Found

    #after redirection, see if the name is on the list
    with app.test_client() as test_client:
        res = test_client.get('/estimate')
        assert res.status_code == 200
        assert 141, 300.00 in res.data   
    
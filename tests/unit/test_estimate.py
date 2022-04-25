import app

def test_maintanace_cost(app, client):
    assert app.estimate(radius=180,height=360) == 141,300.00
        
    
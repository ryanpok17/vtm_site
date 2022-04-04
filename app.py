from cmath import pi
from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Mike Colbert", "email":"mike@mike.com" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Home Page')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle='estimate')

@app.route('/vtm_estimate', methods=['GET', 'POST'])
def vtm_estimate():
    if request.method == 'POST':
        form = request.form
        Tradius = form['Tradius']
        Theight = form['Theight']
        tank_top = pi * (Tradius*Tradius)
        tank_side = 2(pi(Tradius*Theight))
        total_area = tank_side + tank_top
        total_sq_ft = total_area/144
        mat_cost = total_sq_ft * 25
        lab_cost = total_sq_ft * 15
        cost = lab_cost + mat_cost
        return redirect(url_for('estimate'))
    return redirect(url_for('estimate'))
    

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect
from flask import render_template, redirect, request, url_for
from flask import request

app = Flask(__name__)

pi=3.14

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance ')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About Vertical Tank Maintenance')

@app.route('/estimate', methods=['GET', 'POST'])
def estimate():
    if request.method=="POST":
        radius= float(request.form['tank_radius'])
        height= float(request.form['tank_height'])
        area_tank_top= pi* radius**2
        area_sides=2*(pi*(radius*height))
        total_area= area_tank_top + area_sides
        square_feet= total_area/144
        material_cost= square_feet*25
        labor_cost= square_feet*15
        total_estimate= material_cost+ labor_cost
        return render_template('estimate.html', pageTitle='Make Estimate', estimate=total_estimate)
    return render_template('estimate.html', pageTitle='Make Estimate')

   


if __name__ == '__main__':
    app.run(debug=True)



#from cmath import pi
#from flask import Flask
#from flask import render_template, redirect, request, url_for

#app = Flask(__name__)

#price=[]

#@app.route('/')
#def index():
    #return render_template('index.html', pageTitle='Home Page')

#@app.route('/about')
#def about():
    #return render_template('about.html', pageTitle='About VTM')

#@app.route('/estimate')
#def estimate():
    #return render_template('estimate.html', pageTitle='estimate',est=price)

#@app.route('/vtm_calc', methods=['GET', 'POST'])
#def vtm_calc():
    #if request.method == 'POST':
        #form = request.form
        #radius = int(form['Tradius'])
        #height = int(form['Theight'])
        #tank_top = pi * (radius*radius)
        #tank_side = ((radius*height)*pi)*2
        #total_area = tank_side + tank_top
        #total_sq_ft = total_area/144
        #mat_cost = total_sq_ft * 25
        #lab_cost = total_sq_ft * 15
        #cost = lab_cost + mat_cost
        #cost = round(cost,2)
        #price.append(cost)
        #return redirect(url_for('estimate'))
    #return redirect(url_for('estimate'))
    

#if __name__ == '__main__':
    #app.run(debug=True)

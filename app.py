from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

friend_list = [{"name": "Mike Colbert", "email":"mike@mike.com" } ]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Mike\'s Friends', friends = friend_list)

@app.route('/mike')
def about():
    return render_template('mike.html', pageTitle='About Mike')

@app.route('/mike')
def estimate():
    return render_template('mike.html', pageTitle='About Mike')

@app.route('/vtm_estimate', methods=['GET', 'POST'])
def vtm_estimate():
    if request.method == 'POST':
        form = request.form
        Tradius = form['Tradius']
        Theight = form['Theight']
        #friend_dict = {"name": fname + " " + lname, "email": email}
        #friend_list.append(friend_dict)
        #return redirect(url_for('index'))
    #return redirect(url_for('index'))
    

if __name__ == '__main__':
    app.run(debug=True)

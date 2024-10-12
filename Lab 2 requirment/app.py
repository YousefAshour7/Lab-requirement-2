from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods= ['POST'])
def submit():
    fname = request.form['first name']
    lname = request.form['last name']
    email = request.form['email']
    phone_num = request.form['number']

    return render_template('result.html', firstname = fname, lastname = lname, email = email, phone_number = phone_num )

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template, Flask, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

class Registration(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    package = db.Column(db.String(50), nullable=False)
    payment_method = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=True)
    adults = db.Column(db.Integer, nullable=False)
    children = db.Column(db.Integer, nullable=True)
    special_requests = db.Column(db.Text, nullable=True)
    
class SubmitFeedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.String(100), nullable=False)
    ideas = db.Column(db.String(100), nullable=False)
       



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/destination.html')
def destination():
    return render_template('destination.html')

@app.route('/tours.html')
def tours():
    return render_template('tours.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/farfooh.html')
def farfooh():
    return render_template("farfooh.html")

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        new_feedback = SubmitFeedback(
            name=request.form['name'],
            email=request.form['email'],
            feedback=request.form['feedback'],
            ideas=request.form['ideas']
        )
        db.session.add(new_feedback)
        db.session.commit()
        flash('Thank you for your feedback!')
        return redirect(url_for('contact'))
    return render_template('contact.html')


@app.route('/Rakaposhi.html')
def Rakaposhi():
    return render_template('Rakaposhi.html')

@app.route('/diran.html')
def diran():
    return render_template('diran.html')

@app.route('/gargoo.html')
def gargoo():
    return render_template('gargoo.html')

@app.route('/barcha.html')
def barcha():
    return render_template('barcha.html')

@app.route('/working.html')
def working():
    return render_template('working.html')

@app.route('/submit_info', methods=['POST'])
def submit_info():
    if request.method == 'POST':
        user_info = request.form['user-info']
        user_pic = request.form['user-pic']
        
        # save the data to a file
        with open('submitted_info.txt', 'a') as f:
            f.write(f"User Info: {user_info}\n")
            f.write(f"User Pic: {user_pic}\n")
            f.write("\n")
            
        # process the data as needed
        return 'Form submitted successfully'
    return redirect(url_for('working'))

@app.route('/register.html', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        new_registration = Registration(
            name=request.form['name'],
            email=request.form['email'],
            phone=request.form['phone'],
            date=request.form['date'],
            package=request.form['package'],
            payment_method=request.form['payment_method'],
            message=request.form.get('message'),
            adults=int(request.form['adults']),
            children=request.form.get('children', 0),
            special_requests=request.form.get('special_requests')
        )
        db.session.add(new_registration)
        db.session.commit()
        flash('Your form has been successfully submitted. We will contact you soon.')
        return redirect(url_for('register'))
    return render_template('register.html')




if __name__ == "__main__":
     with app.app_context():
          db.create_all()
     app.run(debug=True)      
         
   

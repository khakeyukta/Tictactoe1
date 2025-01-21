from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Game(db.Model):
     User_id=db.Column(db.String(200),primary_key=true)
     password=db.Column(db.String,nullable=False)

def __repr__(self)->str:
     return f"{self.sno} - {self.User_Id}"
     
     
      


@app.route('/')
def tictacttoe():
     return render_template("index.html")

# @app.route('/login')
# def log():
#      return render_template("login_form.html")

# def login():
@app.route('/login', methods=['GET', 'POST'])    
def login():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']

        # Check if user exists in the database
        user = Game.query.filter_by(userid=userid).first()

        if user and user.password == password:
            # Login successful
            return render_template("game.html")
        else:
            # Login failed
            flash('Invalid User ID or Password. Please try again.')
            return redirect(url_for('login'))

    return render_template("game.html")

# @app.route('/reg')
# def reg():
#       return render_template("reg_form.html")
# def register():
#     userid= request.form['userid']
#     password = request.form['password']

#     # Save to database
#     new_user = Game(userid=userid, password=password)
#     db.session.add(new_user)
#     db.session.commit()

#     return "User registered successfully!"

@app.route('/reg', methods=['GET', 'POST'])
def reg():
    return render_template("reg_form.html")

def register():
    if request.method == 'POST':
        userid = request.form['userid']
        password = request.form['password']

        # Save to database
        new_user = Game(userid=userid, password=password)
        db.session.add(new_user)
        db.session.commit()

        return "User registered successfully!"
    return render_template("login_form.html")




if __name__ == "__main__":
    app.run(debug=True)

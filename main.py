from flask import Flask ,render_template,request,redirect,url_for
from database.database import *





app=Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')




@app.route('/register',methods=['GET','POST'])
def register():
    email=request.form.get('email')
    password=request.form.get('password')
    
    if email and password:
        try:
            user=User.create(email=email,password=password)
            return redirect(url_for('login'))
        except  Exception as e : 
            return redirect(url_for('register'))

    return render_template('register.html')








@app.route('/login',methods=['GET','POST'])
def login():
    email=request.form.get('email')
    password=request.form.get('password')

    try:
        if email and password:
            usuario = (User.get(User.email == email)) and (User.get(User.password == password))
            print(usuario)
            return redirect('http://localhost:5173')
    except Exception as e :
        return redirect(url_for('register'))

    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)

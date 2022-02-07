from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():
     return render_template('home.html')
 



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login.html')
def login():
    return render_template('login.html')


@app.route('/signup.html')
def signup():
    return render_template('signup.html')


@app.route('/count.html')
def count():
    return render_template('count.html')



@app.route('/logout.html')
def logout():
    return render_template('logout.html')



@app.route('/contact')
def contactme():
    return render_template('contactme.html')





if __name__ == '__main__':
    app.run(debug=True)

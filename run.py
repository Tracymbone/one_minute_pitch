from flask import Flask, render_template

app=Flask(__name__)

@app.route('/home')
def home():
     return render_template('home.html')
 


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact')
def contactme():
    return render_template('contactme.html')





if __name__ == '__main__':
    app.run(debug=True)

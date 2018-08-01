from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

@app.route('/matematica')
def matematica():
    return render_template('Matematica.html')

@app.route('/portugues')
def portugues():
    return render_template('Portugues.html')

@app.route('/ingles')
def ingles():
    return render_template('Ingles.html')

@app.route('/quimica')
def quimica():
    return render_template('Quimica.html')

@app.route('/fisica')
def fisica():
    return render_template('Fisica.html')

app.run(debug=True)

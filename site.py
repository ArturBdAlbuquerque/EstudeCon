from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')

#MATEMÁTICA--INÍCIO

@app.route('/matematica')
def matematica():
    return render_template('Matematica.html')

@app.route('/multiplos_divisores')
def multiplos_divisores():
    return render_template('multiplos_divisores.html')

@app.route('/regra_de_tres')
def regra_de_tres():
    return render_template('regra_de_tres.html')

@app.route('/algarismos_romanos')
def algarismos_romanos():
    return render_template('algarismos_romanos.html')

@app.route('/razoes_proporcoes')
def razoes_proporcoes():
    return render_template('razoes_proporcoes.html')

@app.route('/fracoes')
def fracoes():
    return render_template('fracoes.html')

@app.route('/numeros_decimais')
def numeros_decimais():
    return render_template('numeros_decimais.html')

@app.route('/aritmetica')
def aritmetica():
    return render_template('aritmetica.html')

@app.route('/radiciacao_potenciacao')
def radiciacao_potenciacao():
    return render_template('radiciacao_potenciacao.html')

@app.route('/algebra')
def algebra():
    return render_template('algebra.html')

@app.route('/funcoes')
def funcoes():
    return render_template('funcoes.html')

@app.route('/medidas_de_tempo')
def medidas_de_tempo():
    return render_template('medidas_de_tempo.html')

@app.route('/sistema_metrico_decimal')
def sistema_metrico_decimal():
    return render_template('sistema_metrico_decimal.html')

@app.route('/equacao_primeiro_grau')
def equacao_primeiro_grau():
    return render_template('equacao_primeiro_grau.html')

@app.route('/equacao_segundo_grau')
def equacao_segundo_grau():
    return render_template('equacao_segundo_grau.html')

@app.route('/angulos')
def angulos():
    return render_template('angulos.html')

@app.route('/porcentagem')
def porcentagem():
    return render_template('porcentagem.html')

@app.route('/poligonos')
def poligonos():
    return render_template('poligonos.html')

@app.route('/geometrias')
def geometrias():
    return render_template('geometrias.html')

@app.route('/calculo_vetorial')
def calculo_vetorial():
    return render_template('calculo_vetorial.html')

@app.route('/inequacoes')
def inequacoes():
    return render_template('inquacoes.html')

#MATEMÁTICA -- FIM


#PORTUGUÊS -- INÍCIO

@app.route('/portugues')
def portugues():
    return render_template('Portugues.html')

#PORTUGUÊS -- FIM


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

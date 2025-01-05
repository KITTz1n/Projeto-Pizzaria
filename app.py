import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import os

lista = []

app = Flask(__name__)

caminho_csv = os.path.join(app.root_path, 'data/diametro.csv')
df = pd.read_csv(caminho_csv)
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x,y)
preco = 0

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/estimativa', methods=['POST'])
def calculo():
    diametro = request.form.get('diam')
    if diametro is not None:
        diametro = int(diametro)
        preco = round(modelo.predict([[diametro]])[0][0])
        return render_template('estimativa.html',base=preco)
    else:
        return render_template('estimativa.html', base='erro!!!')   
    
@app.route('/total', methods=['POST'])
def total():
    caminho_csv2 = os.path.join(app.root_path, 'data/sabor.csv')
    sabores = pd.read_csv(caminho_csv2)
    for adicional in sabores['adicional']:
        if adicional not in lista:
            lista.append(adicional)

if __name__ == '__main__':
    app.run(debug=True)
import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
caminho_csv = os.path.join(app.root_path, 'data/diametro.csv')
df = pd.read_csv(caminho_csv)
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x,y)

caminho_csv2 = os.path.join(app.root_path, 'data/sabor.csv')
sabores_df = pd.read_csv(caminho_csv2)

@app.route('/', methods=['GET', 'POST'])
def inicio():
    return render_template('index.html', tabela=df.to_html(classes='tabela'))

@app.route('/total', methods=['GET','POST'])
def total():
    diametro = request.form.get('diam')
    sabor = request.form.get('sabor')
    preco_diam = None
    if diametro:
        diametro = int(diametro)
        preco_diam = round(modelo.predict(pd.DataFrame([[diametro]], columns=['diametro']))[0][0])
    preco_total = 0

    if sabor:
        sabor_encontrado = sabores_df[sabores_df['sabor'].str.lower() == sabor.lower()]
        if not sabor_encontrado.empty:
            adicional = sabor_encontrado['adicional'].values[0]
            preco_total = round(preco_diam + adicional, 2)
        else:
            adicional = "Sabor não encontrado!"
            preco_total = preco_diam
    else:
        adicional = "Sabor não selecionado!"
        preco_total = preco_diam

    return render_template('total.html', sabor=sabor.capitalize() if sabor else "Nenhum sabor", adicional=adicional,preco=preco_diam, preco_total=preco_total)
    
if __name__ == '__main__':
    app.run(debug=True)
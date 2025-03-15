import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
import os

app = Flask(__name__)
caminho_csv = os.path.join(app.root_path, 'data/diametro.csv')
df = pd.read_csv(caminho_csv)
modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]
modelo.fit(x,y)
preco = 0
caminho_csv2 = os.path.join(app.root_path, 'data/sabor.csv')
sabores_df = pd.read_csv(caminho_csv2)
diametro = None
preco

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/estimativa', methods=['POST'])
def estimativa():
    # Aqui pegamos o diâmetro enviado do formulário
    diametro = request.form.get('diam')
    preco = None
    if diametro:
        diametro = int(diametro)
        preco = round(modelo.predict(pd.DataFrame([[diametro]], columns=['diametro']))[0][0])
        return render_template('estimativa.html', base=preco)
    else:
        return render_template('index.html', erro='Erro! Insira um valor válido para o diâmetro.')
    
@app.route('/total', methods=['GET', 'POST'])
def total():
    adicional = None
    erro = None
    if request.method == 'POST':
        sabor = request.form.get('sabor')
        
        # Verifica se o sabor existe na base de dados
        sabor_encontrado = sabores_df[sabores_df['sabor'].str.lower() == sabor.lower()]

        if not sabor_encontrado.empty:
            adicional = sabor_encontrado['adicional'].values[0]  # Pega o valor do adicional
        else:
            erro = "Sabor não encontrado!"  # Se não encontrar, exibe erro

    # Verifica se as variáveis estão definidas antes de fazer o cálculo
    if adicional is not None and preco is not None:
        preco_total = round(float(preco) + float(adicional), 2)
        return render_template('total.html', adicional=adicional, erro=erro, preco_total=preco_total)
    else:
        return render_template('total.html', erro="Erro no cálculo. Verifique os dados.")
    
if __name__ == '__main__':
    app.run(debug=True)
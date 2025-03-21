import pandas as pd
from flask import Flask, render_template, request, redirect, session
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
modelo.fit(x, y)

caminho_csv2 = os.path.join(app.root_path, 'data/sabor.csv')
sabores_df = pd.read_csv(caminho_csv2)

@app.route('/', methods=['GET', 'POST'])
def inicio():

    numero_pizzaria = request.args.get('numero', '000000000000')
    
    tabela_html = "<table class='tabela'>"
    tabela_html += "<tr><th class='borda-esq'>Sabor</th><th class='borda-dir'>Adicional</th></tr>"

    for _, row in sabores_df.iterrows():
        tabela_html += f"<tr><td class='borda-esq'>{row['sabor']}</td><td class='borda-dir'>{row['adicional']}</td></tr>"

    tabela_html += "</table>"

    return render_template('index.html', tabela=tabela_html, numero_pizzaria=numero_pizzaria)

@app.before_request
def before_request():
    if 'numero' in request.args:  # Se o número foi passado na URL
        session['numero_pizzaria'] = request.args.get('numero')

@app.route('/editar_msg', methods=['GET', 'POST'])
def editar_msg():
    diametro = request.form.get('diam')
    sabor = request.form.get('sabor')
    endereco = request.form.get('endereco')

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

    mensagem_padrao = f"Ola, gostaria de pedir uma pizza de {sabor} com {diametro} cm, endereco: {endereco}"
    
    return render_template('editar_msg.html', sabor=sabor.capitalize() if sabor else "Nenhum sabor", adicional=adicional, preco=preco_diam, preco_total=preco_total, mensagem=mensagem_padrao)

@app.route('/enviar_msg', methods=['GET','POST'])
def enviar_msg():
    numero_pizzaria = session.get('numero_pizzaria', '000000000000')  # Pegando da sessão
    mensagem = request.form.get('mensagem')
    url_whatsapp = f"https://wa.me/{numero_pizzaria}?text={mensagem}"
    return redirect(url_whatsapp)

if __name__ == '__main__':
    app.run(debug=True)

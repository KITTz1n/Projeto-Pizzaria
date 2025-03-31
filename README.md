# Projeto Site para Pizzaria

## Sobre o Projeto
Este projeto foi desenvolvido utilizando **Python** e o framework **Flask**. Ele permite calcular o preço de uma pizza com base no diâmetro e no sabor escolhido, além de gerar uma mensagem automática para pedido via WhatsApp.

🔗 **Veja o projeto funcionando**: [Projeto Pizzaria](https://projeto-pizzaria.onrender.com)

---

## Instalação e Execução

### 📌 Requisitos
Antes de iniciar, certifique-se de ter instalado:
- **Python 3.x**
- **Gerenciador de pacotes `pip`**

### 📥 Instalando Dependências
Abra um terminal na pasta do projeto e execute:
```sh
pip install pandas matplotlib flask scikit-learn
```

### 🚀 Executando o Projeto

1. Localize o arquivo `app.py` na estrutura de pastas:
   ```
   |—— .gitattributes
   |—— app.py  <-- AQUI!!!      
   |—— data           
   |    |—— diametro.csv
   |    |—— sabor.csv
   |—— static
   |    |—— all.css
   |    |—— imagens
   |        |—— pizza_img1.jpg
   |—— templates
   |    |—— estimativa.html
   |    |—— index.html
   |—— treino.ipynb
   ```
2. No terminal, navegue até a pasta do projeto:
   ```sh
   cd caminho/para/Pizzaria_Projeto
   ```
3. Execute o arquivo:
   ```sh
   python app.py
   ```
   Ou, se precisar usar uma versão específica do Python:
   ```sh
   py -VERSAO_DO_PYTHON_AQUI app.py
   ```

### 🖥️ Executando via VS Code ou IDE
Se estiver usando o **VS Code** ou outra IDE, clique no botão de **Run File** no canto superior direito.

---

## Acessando o Projeto
Após a execução, o terminal mostrará algo como:
```sh
 * Running on: http://127.0.0.1:5000/  <--------------
```
Clique no link para acessar o site.

⚠️ **Nota**: Esse servidor é para desenvolvimento. Para produção, use um WSGI server como Gunicorn.

---

Feito com ❤️ para facilitar pedidos de pizza! 🍕
<h1>Projeto site para pizzaria</h1>
<h3>Sobre o projeto</h3>
<p> Esse projeto foi desenvolvido com python usando uma biblioteca chamada Flask
</p>
<h3>Instalando Bibliotecas</h3>
<p>Caso tenha um Source Code Editor ou uma IDE <br> Abra ele e no seu terminal digite o seguinte comando</p>

<pre><code>pip install pandas, matplotlib, flask, sklearn</code></pre>

<p>Caso não tenha, minha recomendação é instalar o VSCode</p>

<h3>Executar</h3>

<p>Primeiramente encontre o arquivo chamado <code>app.py</code></p>

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

<p>Para executar ele temos duas formas<br>
<ul>
<li>
<h5>Executando-o pelo terminal do Source Code Editor ou IDE</h5>
Primeiramente veja se o terminal esta na pasta do projeto, deve estar assim aproximadamente<br>
<code>C:\Users\Name_User\Pasta1\Pasta2\Pizzaria_Projeto></code><br>
Caso de estar so na ate a Pasta2 digite o seguinte<br>
<code>C:\Users\Name_User\Pasta1\Pasta2> cd Pizzaria_Projeto</code><br>
após temos como fazer de 2 formas também:
<ul>
<li><h5>Diretamente pelo python</h5>
Digite o seguinte comando: <br>
<code>C:\Users\Name_User\Pasta1\Pasta2\Pizzaria_Projeto> python app.py</code><br>
E ira rodar o codigo<br>
</li>
<li><h5>Versão Específica do python</h5>
Caso queira executar em uma versão específica do python de o seguint comando:<br>
<code>C:\Users\Name_User\Pasta1\Pasta2\Pizzaria_Projeto> py -VERSAO_DO_PYTHON_AQUI app.py</code>
</li>
</ul>
</li>
<li>
<h5>Executando-o pelo proprio Source Code Editor ou IDE</h5>
No caso de quem usa VSCode ou algo parecido deve exitir um símbolo de Run File no canto superior direito <br>
<img src="https://github.com/user-attachments/assets/c578b8c6-9417-4acc-af38-e42bcd91c430" alt="exemplo"></img>
</li>
</ul>
<h3>Após a execução</h3>
Após você executar o código aparecera no terminal da seguinte maneira:<br>

```
PS C:\Users\Name_User\Pasta1\Pasta2> & "C:/Program Files/Python312/python.exe" c:/Users/Name_User/Pasta1/Pasta2/Pizzaria_Projeto/app.py
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on: LINK_VAI_ESTAR_AQUI <--------------
Press CTRL+C to quit
 * Restarting with watchdog (windowsapi)
 * Debugger is active!
 * Debugger PIN: NUMBER-PIN
```

Clique no link e após isso você vera o site funcionando

<h2>Imagens do site</h2>
<img src="https://github.com/user-attachments/assets/485f70b2-c268-47d0-aa6a-9d65183059d5" alt="exemplo celular">
<br>
<img src="https://github.com/user-attachments/assets/8f80fd19-a39d-46a5-a1ac-17ba05d86122" alt="exemplo pc"> SENDO FEITO PARA PC AINDA!!!
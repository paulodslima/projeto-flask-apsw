from flask import Flask, render_template
from config import db
from usuario import Usuario

TEMPLATE = './templates'

STATIC = './static'

app = Flask(__name__, template_folder=TEMPLATE, static_folder=STATIC )

# Configuraçã de banco de dados
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///./dados.db'
db.init_app(app)

with app.app_context():
    db.create_all()
 
#Definição das rotas
@app.route('/')
def helloWorld():
    return 'hello World'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/cadastrarUsuario')
def cadastrarUsuario():
    usuario = Usuario('Flavio medeiros', 'flaviomedeiros@ifal.edu.br')
    db.session.add(usuario)
    db.session.commit()
    return 'Usuario cadastrado com sucesso'

@app.route('/consultarUsuarios')
def consultarUsuarios():
    usuarios = Usuario.query.all()
    return render_template('mostrarUsuarios.hmtl', usuarios=usuarios)

app.run(host='0.0.0.0', port=5000)
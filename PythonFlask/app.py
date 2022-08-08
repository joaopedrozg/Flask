from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'

db = SQLAlchemy(app)

frutas = []
registros = []

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)
    
    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch
		



@app.route('/', methods=['GET', 'POST'])
def principal():
	#frutas = ['Morango', 'Uva', 'Laranja', 'Mamão', 'Maçã', 'Melão', 'Abacaxi', 'Melancia ' ]

	if request.method == 'POST':
		if request.form.get('fruta'):
			frutas.append(request.form.get('fruta'))
	
	return render_template('index.html', frutas = frutas)


@app.route('/sobre', methods=['GET', 'POST'])
def sobre():
	#notas = {'Fulano':5.0, 'Beltrano':6.0, 'Aluno':7.0, 'Sicrano':8.5}
	if request.method == 'POST':
		if request.form.get('aluno') and request.form.get('nota'):
			registros.append({'aluno': request.form.get('aluno'), 'nota': request.form.get('nota')})


	return render_template('sobre.html', registros = registros)



@app.route('/cursos')
def lista_cursos():
    return render_template('cursos.html', cursos = cursos.query.all())
	
    
@app.route('/cria_cursos') 
def cria_curso():
    return render_template('novo_curso.html')   
    
if __name__ == '__main__':
	db.create_all()
	app.run(debug=True)
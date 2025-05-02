from config import app,db
from controllers.alunosRoute import aluno_blueprint
from controllers.professorRoute import professor_blueprint
from controllers.turmaRoute import turma_blueprint

app.register_blueprint(aluno_blueprint)
app.register_blueprint(professor_blueprint)
app.register_blueprint(turma_blueprint)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
  app.run(host=app.config["HOST"], port = app.config['PORT'],debug=app.config['DEBUG'] )
import unittest
from app import app, db

class TestApp(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # --- PROFESSORES ---

    def test_001_add_professor(self):
        data = {
            'nome': 'John Doe',
            'idade': 30,
            'materia': 'Matemática',
            'observacoes': 'Muito bom!'
        }
        response = self.app.post('/professores', json=data)
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json)

    def test_002_get_professores(self):
        self.test_001_add_professor()
        response = self.app.get('/professores')
        self.assertEqual(response.status_code, 200)

    def test_003_get_professor(self):
        response = self.app.post('/professores', json={
            'nome': 'Jane Smith', 'idade': 35, 'materia': 'Física', 'observacoes': ''
        })
        pid = response.json['id']
        response = self.app.get(f'/professores/{pid}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['nome'], 'Jane Smith')

    def test_004_update_professor(self):
        response = self.app.post('/professores', json={
            'nome': 'Carlos Silva', 'idade': 40, 'materia': 'Química', 'observacoes': ''
        })
        pid = response.json['id']
        response = self.app.put(f'/professores/{pid}', json={
            'nome': 'Carlos S.', 'idade': 41, 'materia': 'Química', 'observacoes': 'Atualizado'
        })
        self.assertEqual(response.status_code, 200)

    def test_005_delete_professor(self):
        response = self.app.post('/professores', json={
            'nome': 'Ana Souza', 'idade': 50, 'materia': 'Biologia', 'observacoes': ''
        })
        pid = response.json['id']
        response = self.app.delete(f'/professores/{pid}')
        self.assertEqual(response.status_code, 200)

    # --- TURMAS ---

    def test_006_add_turma(self):
        professor = self.app.post('/professores', json={
            'nome': 'Prof. Turma', 'idade': 45, 'materia': 'Geografia', 'observacoes': ''
        }).json
        response = self.app.post('/turmas', json={
            'descricao': 'Turma A', 'professor_id': professor['id'], 'ativo': True
        })
        self.assertEqual(response.status_code, 201)

    def test_007_get_turmas(self):
        self.test_006_add_turma()
        response = self.app.get('/turmas')
        self.assertEqual(response.status_code, 200)

    def test_008_get_turma(self):
        professor = self.app.post('/professores', json={
            'nome': 'Prof. T8', 'idade': 45, 'materia': 'Geo', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma B', 'professor_id': professor['id'], 'ativo': True
        }).json
        response = self.app.get(f"/turmas/{turma['turma_id']}")
        self.assertEqual(response.status_code, 200)

    def test_009_update_turma(self):
        professor = self.app.post('/professores', json={
            'nome': 'Prof. T9', 'idade': 45, 'materia': 'História', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma C', 'professor_id': professor['id'], 'ativo': False
        }).json
        response = self.app.put(f"/turmas/{turma['turma_id']}", json={
            'descricao': 'Turma C Atualizada', 'professor_id': professor['id'], 'ativo': True
        })
        self.assertEqual(response.status_code, 200)

    def test_010_delete_turma(self):
        professor = self.app.post('/professores', json={
            'nome': 'Prof. T10', 'idade': 50, 'materia': 'Ed. Física', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma D', 'professor_id': professor['id'], 'ativo': True
        }).json
        response = self.app.delete(f"/turmas/{turma['turma_id']}")
        self.assertEqual(response.status_code, 200)

    # --- ALUNOS ---

    def test_011_add_aluno(self):
        prof = self.app.post('/professores', json={
            'nome': 'Prof. A1', 'idade': 38, 'materia': 'Biologia', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma Aluno', 'professor_id': prof['id'], 'ativo': True
        }).json
        response = self.app.post('/alunos', json={
            'nome': 'Joaquim', 'idade': 18, 'turma': turma['turma_id'],
            'data_nasc': '2000-01-01', 'nota_primeiro_sem': 8.5, 'nota_segundo_sem': 9.5
        })
        self.assertEqual(response.status_code, 201)

    def test_012_get_alunos(self):
        self.test_011_add_aluno()
        response = self.app.get('/alunos')
        self.assertEqual(response.status_code, 200)

    def test_013_get_aluno(self):
        prof = self.app.post('/professores', json={
            'nome': 'Prof. A3', 'idade': 39, 'materia': 'História', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma A3', 'professor_id': prof['id'], 'ativo': True
        }).json
        aluno = self.app.post('/alunos', json={
            'nome': 'Lucas', 'idade': 20, 'turma': turma['turma_id'],
            'data_nasc': '2001-05-10', 'nota_primeiro_sem': 7.5, 'nota_segundo_sem': 8.0
        }).json
        response = self.app.get(f"/alunos/{aluno['aluno_id']}")
        self.assertEqual(response.status_code, 200)

    def test_014_update_aluno(self):
        prof = self.app.post('/professores', json={
            'nome': 'Prof. A4', 'idade': 40, 'materia': 'Português', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma A4', 'professor_id': prof['id'], 'ativo': True
        }).json
        aluno = self.app.post('/alunos', json={
            'nome': 'Carlos', 'idade': 22, 'turma': turma['turma_id'],
            'data_nasc': '1999-08-15', 'nota_primeiro_sem': 9.0, 'nota_segundo_sem': 8.5
        }).json
        response = self.app.put(f"/alunos/{aluno['aluno_id']}", json={
            'nome': 'Carlos Silva', 'idade': 23, 'turma': turma['turma_id'],
            'data_nasc': '1999-08-15', 'nota_primeiro_sem': 8.0, 'nota_segundo_sem': 9.0
        })
        self.assertEqual(response.status_code, 200)

    def test_015_delete_aluno(self):
        prof = self.app.post('/professores', json={
            'nome': 'Prof. A5', 'idade': 41, 'materia': 'Artes', 'observacoes': ''
        }).json
        turma = self.app.post('/turmas', json={
            'descricao': 'Turma A5', 'professor_id': prof['id'], 'ativo': True
        }).json
        aluno = self.app.post('/alunos', json={
            'nome': 'Maria', 'idade': 19, 'turma': turma['turma_id'],
            'data_nasc': '2001-03-25', 'nota_primeiro_sem': 6.5, 'nota_segundo_sem': 7.5
        }).json
        response = self.app.delete(f"/alunos/{aluno['aluno_id']}")
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main(verbosity=2)
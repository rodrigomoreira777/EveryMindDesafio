from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    codigo = db.Column(db.String(50), nullable=False, unique=True)
    descricao = db.Column(db.String(200))
    preco = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Produto %r>' % self.nome
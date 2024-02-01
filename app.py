from flask import Flask, render_template, request, redirect, url_for
from models import db, Produto

app = Flask(__name__)

# Configurando o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:SENHA@localhost/base_de_dados'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


# Inserindo rotas CRUD
@app.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', produtos=produtos)


@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        nome = request.form['nome']
        codigo = request.form['codigo']
        descricao = request.form['descricao']
        preco = request.form['preco']

        novo_produto = Produto(nome=nome, codigo=codigo, descricao=descricao, preco=preco)
        db.session.add(novo_produto)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add_product.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_product(id):
    produto = Produto.query.get_or_404(id)

    if request.method == 'POST':
        produto.nome = request.form['nome']
        produto.codigo = request.form['codigo']
        produto.descricao = request.form['descricao']
        produto.preco = request.form['preco']

        db.session.commit()
        return redirect(url_for('index'))

    return render_template('edit_product.html', produto=produto)


@app.route('/delete/<int:id>')
def delete_product(id):
    produto = Produto.query.get_or_404(id)
    db.session.delete(produto)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/show/<int:id>')
def show_product(id):
    produto = Produto.query.get_or_404(id)
    return render_template('show_product.html', produto=produto)


if __name__ == '__main__':
    app.run(debug=True)

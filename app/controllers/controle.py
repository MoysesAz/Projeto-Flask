from app import app, render_template, request, redirect, url_for, db, abort
from app.models.tables import User


@app.route('/')
def Home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            user = User.query.filter(User.username == username).first()
            if not user:
                status_index = 'Usuário não cadastrados'
                return render_template('index.html', status_index=status_index)
            elif (password == user.password):
                return f"{username} é um cadastrado!!!"
            else:
                status_index = 'Password inválido'
                return render_template('index.html', status_index=status_index)
        except NameError:
            return NameError


@app.route('/cadastrar', methods=['GET', 'POST'])
def Cadastro():
    if request.method == 'GET':
        return render_template('cadastro.html')

    if request.method == 'POST':
        try:
            username = request.form['username']
            email = request.form['username']
            teste_user = User.query.filter(User.username == username).first()
            teste_email = User.query.filter(User.username == email).first()
            if not teste_user and not teste_email:
                cadastro = User(
                    request.form['username'],
                    request.form['password'],
                    request.form['nome'],
                    request.form['email'],
                )
                db.session.add(cadastro)
                db.session.commit()
                status_index = 'Cadastro efetuado com sucesso'
                return render_template('index.html', status_index=status_index)
            else:
                status_cadastro = 'Login ou  Email já cadastrados'
                return render_template('cadastro.html', status_cadastro=status_cadastro)
        except :
            return abort(404)



@app.route('/tabela')
def Tabela():
    cadastrados = (User).query.all()
    return render_template('tabela.html', cadastrados=cadastrados)


@app.route('/delete/<int:id>')
def delete(id):
    cadastrados = (User).query.get(id)
    db.session.delete(cadastrados)
    db.session.commit()
    return redirect(url_for('Tabela'))

from flask import flash, render_template, session, request,redirect, url_for

from loja import app, db, bcrypt
from loja.admin.forms import RegistrationForm


@app.route('/')

def home():
    return "Bem vindo ao sistema em flask"

@app.route('/registrar', methods=['GET','POST '])
def registrar():
    form = RegistrationForm(request.form)
    if request.method =='POST' and form.validate():



        flash('Registro feito com sucesso!')
        return redirect(url_for('Login'))
    return render_template('admin/registrar.html' , form=form ,title="Registrar usuários")


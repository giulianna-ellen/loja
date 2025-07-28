from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    nome = StringField('Nome Completo:',[validators.Length(min=10, max= 100)])
    usuario = StringField('Usuário:', [validators.Length(min=4 , max=25)])
    email = StringField('Email:', [validators.Length(min=10, max= 50)])
    senha= PasswordField('Nova Senha:', [
        validators.DataRequired(),
        validators.EqualTo('Confirme', message='As senhas devem ser iguais')
    ])
    confirme = PasswordField('Confirme a senha digitando novamente')
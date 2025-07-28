from loja import db

class Cliente(db.Model):
    id= db.Column(db.Integer, prymary_key=True)
    nome= db.Column(db.String(80), unique=True, nullable=False)
#adicionar as informações




    def __repr__ (self):
        return'<Cliente %r>' %self.username
    #esse username tem que mudar provavelmente
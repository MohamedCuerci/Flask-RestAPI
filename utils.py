from models import PessoasTeste, Usuarios

#insere dados
def insere_pessoas():
    pessoa = PessoasTeste(nome='Lucas', idade=22)
    print(pessoa)
    pessoa.save()

#consulta os dados
def consulta_pessoas():
    #pessoa = PessoasTeste.query.all()
    pessoa = PessoasTeste.query.filter_by(nome='lucas')
    print(pessoa.nome)

#altera dados
def altera_pessoa():
    pessoa = PessoasTeste.query.filter_by(nome='Lucas')
    pessoa.idade = 21
    pessoa.save()

#exclui dados
def exclui_pessoa():
    pessoa = PessoasTeste.query.filter_by(nome='').first()
    pessoa.delete()


def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)



if __name__ == '__main__':
    #insere_pessoas()
    #consulta_pessoas()
    insere_usuario('lucas', '1234')
    insere_usuario('cuerci', '4321')
    consulta_todos_usuarios()




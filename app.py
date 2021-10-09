from flask import Flask, request
from flask_restful import Resource, Api
from models import PessoasTeste, Atividade, Usuarios
from flask_httpauth import HTTPBasicAuth


auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)


usuarios = {
    'Lucas': 123,
    'Cuerci': 321
    }

#decorador - verificador de senha
@auth.verify_password
def verificacao(login, senha):
    #se a senha e login foem diferentes ele retornara False
    if not (login, senha):
        return False
    return Usuarios.query.filter_by(login=login, senha=senha).first()



class Pessoa(Resource):
    #obriga estar logado para poder acessar
    @auth.login_required
    def get(self, nome):
        pessoa = PessoasTeste.query.filter_by(nome=nome).first()
        try:
            response = {
                'nome': pessoa.nome,
                'idade': pessoa.idade,
                'id': pessoa.id
            }
        except AttributeError:
            response = {
                'status': 'error',
                'mensagem': 'Pessoa não encontrada'

            }
        return response

    def put(self, nome):
        pessoa = PessoasTeste.query.filter_by(nome=nome).first()
        dados = request.json
        if 'nome' in dados:
            pessoa.nome = dados['nome']
        if 'idade' in dados:
            pessoa.idade = dados['idade']
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response


    def delete(self, nome):
        pessoa = PessoasTeste.query.filter_by(nome=nome).first()
        mensagem = f'Pessoa {pessoa.nome} foi excluida com sucesso'
        pessoa.delete()
        return {'status': 'sucesso', 'mensagem': mensagem}


class ListaPessoas(Resource):
    @auth.login_required
    def get(self):
        #.all() - lista tudo
        #.filter_by() seleciona algo especifico
        pessoas = PessoasTeste.query.all()
        response = [{'id': i.id, 'nome': i.nome, 'idade': i.idade} for i in pessoas]
        return response

    def post(self):
        dados = request.json
        pessoa = PessoasTeste(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response

class ListaAtividade(Resource):
    @auth.login_required
    def get(self):
        atividades = Atividade.query.all()
        response = [{'id':i.id, 'nome': i.nome, 'pessoa': i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = PessoasTeste.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividade(nome=dados['nome'], pessoas=pessoa)
        response = {
            'pessoa': atividade.pessoa.nome,
            'nome': atividade.nome,
            'id': atividade.id
        }


api.add_resource(Pessoa, '/pessoa/<string:nome>/')
api.add_resource(ListaPessoas, '/pessoa/')


if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify
from flask_restful import Resource, Api
import json, requests

desenvolvedores = [

    {
        'id': '0',
        'nome': 'Cuerci',
        'habilidade': ['Python', 'Flask']
    },
    {
        'id': '1',
        'nome': 'Soares',
        'habilidade': ['Java', 'Django']
    },
{
        'id': '2',
        'nome': 'Mohamed',
        'habilidade': ['javascript', 'Html']
    }
]

app = Flask(__name__)
api = Api(app)

class Desenvolvedor(Resource):
    def get(self, id):
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvovledor de ID {id}, não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido, procure pelo administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return response


    def post(self, id):
        return {'nome': 'Lucas'}
    def put(self):
        dados = json.loads(requests.data)
        desenvolvedores[id] = dados
        return dados
        #return {'nome':'Lucas'}

    def delete(self, id):
        desenvolvedores.pop(id)
        return {'status': 'sucesso', 'mensagem': 'Registro excluido'}

#Listar todos os desenvolvedores e oermitir registrar um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return  desenvolvedores

    def post(self):
        dados = json.loads(requests.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return desenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(ListaDesenvolvedores, '/dev/')

if __name__ == '__main__':
    app.run(debug=True)

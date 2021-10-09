from sqlalchemy import create_engine, Integer, String, Column, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///atividades.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autommit=False,
                                         binds=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class PessoasTeste(Base):
    #__tablename__ = nome da coluna
    __tablename__='pessoas'  #nome da tabela
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    #__repr__ = representação
    def __repr__(self):
        return f'<Pessoa {self.nome}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Atividade(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('PessoasTeste')

    # __repr__ = representação
    def __repr__(self):
        return f'<Atividade {self.nome}'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    login = Column(String(20), unique=True)
    senha = Column(String(20))

    def __repr__(self):
        return f'<Usuario {self.login}>'

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()



def init_db():
    #esse comando cria o banco de dados
    Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    init_db()








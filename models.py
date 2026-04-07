# Models é o arquivo onde fica as classes
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

engine = create_engine("sqlite:///escola.db")

Session = sessionmaker(bind=engine)

#Tabelas Cursos e Alunos (1:N)

class Curso(Base):
    __tablename__ = "cursos"

    id_curso = Column(Integer, primary_key=True, autoincrement=True)
    nome_curso = Column(String(100), nullable=False)
    carga_hr = Column(Integer, nullable=False)
    
    alunos = relationship("Aluno", back_populates= "cursos")

    def __repr__(self):
        return f"Curso = ID: {self.id_curso} | Nome: {self.nome} | Carga Horária: {self.carga_hr}"

class Aluno(Base):
    __tablename__ = "alunos"

    id_aluno = Column(Integer, primary_key=True, autoincrement=True)
    nome_aluno = Column(String(100), nullable=False)
    email = Column(String(100), unique=True)
    
    curso_id = Column(Integer, ForeignKey("cursos.id_curso"))

    cursos = relationship("Curso", back_populates= "alunos")

    def __repr__(self):
        return f"Aluno = ID: {self.id_aluno} | Nome: {self.nome_aluno} | Email: {self.email}"


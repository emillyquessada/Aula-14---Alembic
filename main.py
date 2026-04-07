from models import Session, Curso, Aluno

# Criar as funções do crud
#Cadastrar curso.

def cadastrar_curso():
    with Session() as session:
        try:
            nome_curso = input("Digite o nome do curso: ").capitalize()
            carga_hr = int(input("Digite a carga horária: "))
            descricao = input("Digite a descrição do curso: ").capitalize()
            curso = Curso(nome_curso= nome_curso, carga_hr = carga_hr, descricao= descricao)
            session.add(curso)
            session.commit()
            print("Curso criado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

cadastrar_curso()
#Cadastrar um aluno no curso.
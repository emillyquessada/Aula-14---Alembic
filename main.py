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

#cadastrar_curso()
#Cadastrar um aluno no curso.

def cadastrar_aluno():
    nome_aluno = input("Digite o nome do aluno: ").strip().capitalize()
    email_aluno = input("Digite o email do aluno: ").strip().capitalize()
    buscar_curso = input(f"Digite o nome do curso do aluno {nome_aluno}: ").strip().capitalize()
    with Session() as session:
        try:
            curso = session.query(Curso).filter_by(nome_curso=buscar_curso).first()
            if curso == None:
                print("Não foi possível encontrar um curso com este nome!")
                return
            else:
                aluno = Aluno(nome_aluno =nome_aluno, email= email_aluno)
            session.add(aluno)
            session.commit()
            print("Aluno criado com sucesso!")
        except Exception as erro:
            session.rollback()
            print(f"Ocorreu um erro {erro}")

cadastrar_aluno()
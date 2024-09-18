from modulo import *

if __name__ == "__main__":
    
    aluno1 = Aluno('','','')

    aluno1.nome = input('Digite o nome do aluno: ')
    aluno1.matricula = input('Digite a matrícula do aluno: ')
    aluno1.cpf = input('Digite o CPF do aluno: ')

    # teste de saída
    #print(aluno1.nome)
    #print(aluno1.matricula)
    #print(aluno1.cpf)
    aluno2 = Aluno('','','')
    aluno2.nome = input('Digite o nome do 2º aluno: ')
    aluno2.matricula = input('Digite a matrícula do 2º aluno: ')
    aluno2.cpf = input('Digite o CPF do 2º aluno: ')

    '''# teste de saída de dados
    print('Aluno 1: \n')
    print(aluno1.nome)
    print(aluno1.matricula)
    print(aluno1.cpf)
    print('Aluno 2: \n')
    print(aluno2.nome)
    print(aluno2.matricula)
    print(aluno2.cpf)
'''

    curso1 = Curso('',0,'')
    curso1.nome = input('Digite o nome do curso: ')
    curso1.duracao = int(input('Digite a duração do curso: '))
    curso1.turno = input('Digite o turno do curso: ')

    curso2 = Curso('',0,'')
    curso2.nome = input('Digite o nome do 2º curso: ')
    curso2.duracao = int(input('Digite a duração do 2º curso: '))
    curso2.turno = input('Digite o turno do 2º curso: ')

    '''print(curso1.nome)
    print(curso1.duracao)
    print(curso1.turno)
'''
    # cadastrando os alunos instanciados no curso instanciado
    aluno1.inscrever_curso(curso1)
    aluno1.inscrever_curso(curso2)
    aluno2.inscrever_curso(curso1)


    # saida de dados
    print(f'\nAluno {aluno1.nome} de matrícula {aluno1.matricula} está inscrito no curso {aluno1.listar_curso()}.')
    print(f'Aluno {aluno2.nome} de matrícula {aluno2.matricula} está inscrito no curso {aluno2.listar_curso()}.')
    print(f'No curso {curso1.nome} estão matriculados os alunos: {curso1.listar_alunos()}.')
    print(f'No curso {curso2.nome} estão matriculados os alunos: {curso2.listar_alunos()}.')
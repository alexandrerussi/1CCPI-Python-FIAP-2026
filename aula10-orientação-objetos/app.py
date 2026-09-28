from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("Paulo", "123456", "Ciência da Computação")

# criar / instanciar 2 disciplinas
model_lin = Disciplina("Modelagem Linear", "Rodolpho")
dsa = Disciplina("Data Structre", "Erick")

# matricular o aluno1 nas 2 disciplinas
aluno1.matricular(model_lin)
aluno1.matricular(dsa)

# adicionar notas do aluno referente a cada disciplina
aluno1.adicionar_nota(model_lin, 10)
aluno1.adicionar_nota(model_lin, 6)
aluno1.adicionar_nota(dsa, 5)
aluno1.adicionar_nota(dsa, 4)

print(aluno1.media_geral())
# TODO: DESAFIO -- FAZER UM MÉTODO DE EXIBIR BOLETIM
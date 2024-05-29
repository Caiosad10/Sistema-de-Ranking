position = ["1º", "2º", "3º"]

posicaoAluno = {"1º": None, "2º": None, "3º": None}

alunos = []


def nomeAlunos():
  print("Nome dos alunos:\n")
  for i in range(1,6):
    nome = input(f"Digite o nome do {i}º aluno: ")
    alunos.append(nome)
    
nomeAlunos()

def posicaoAlunos():
  print("\nPosições:\n")
  for posicao in position:
    print(f"{posicao} - ")

posicaoAlunos()

def escolhaPosicao():
  for i in range(1,4):
    posicao = position[i-1]
    pos = input(f"\nDiga quem ficou em {posicao} lugar: \n")
    
    if posicaoAluno[position[i-1]] is None:
      posicaoAluno[position[i-1]] = pos
      print(f"{posicao} - {pos}")
    else:
      print("Erro")

escolhaPosicao()
print(posicaoAluno)
    
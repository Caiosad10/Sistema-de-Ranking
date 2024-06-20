import dados

#Função para adicionar alunos
def nomeAlunos():
  print("Nome dos alunos(É necessario no minimo três(3) nomes para determinar o Ranking):\n")
  #Variavel para numerar a quantidade de alunos
  i = 1

  #Loop para adicionar os nomes dos alunos sem ter um limite em mente
  while True:
    nome = input(f'Digite o nome do {i}º aluno ou digite "s" para sair: ')
    if nome.lower() == "s":
      if len(dados.alunos) == 0:
        print("\n\t\tLista vazia")
        break
      else:
        print(f"\nLista encerrada. Foi adicionado {i - 1} alunos!")
        break
    else:
      dados.alunos.append(nome)
    i += 1

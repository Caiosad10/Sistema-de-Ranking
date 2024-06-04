#Quantidade de posição
position = ["1º", "2º", "3º"]

#Dicionario para armazenar os dados com as respectivas posições
posicaoAluno = {"1º": None, "2º": None, "3º": None}

#Lista para armazenar alunos
alunos = []

#Função para adicionar alunos
def nomeAlunos():
  print("Nome dos alunos(É necessario no minimo três(3) nomes para determinar o Ranking):\n")
  #Variavel para numerar a quantidade de alunos
  i = 1
  
  #Loop para adicionar os nomes dos alunos sem ter um limite em mente
  while True:
    nome = input(f'Digite o nome do {i}º aluno ou digite "s" para sair: ')
    if nome.lower() == "s":
      if len(alunos) == 0:
        print("\n\t\tLista vazia")
        break
      else:
        print(f"\nLista encerrada. Foi adicionado {i - 1} alunos!")
        break
    else:
      alunos.append(nome)
    i += 1

def listaAlunos():
  print("\nLista de alunos:\n")
  if len(alunos) == 0:
    print("\t\tLista vazia!\n\nNenhum aluno adicionado ainda!\n\n")
  for i, aluno in enumerate(alunos):
    print(f"{i + 1} - {aluno}")

#Função para mostrar as posições disponiveis
def ranking():
  print("\nPosições:\n")
  for posicao in position:
    print(f"{posicao} - ")


#Função para determinar a posição dos alunos
def escolhaPosicao():
  if len(alunos) == 0:
    print("\n\t\tLista vazia!, impossivel determinar posições!")
  elif len(alunos) < 3:
    print("\n\t\tQuantidade insuficiente de alunos para determinar as posições!")
  elif len(alunos) >= 3:
  
  #Loop para criar uma variavel que percorre a lista de posição
    for i in range(1,4):
      posicao = position[i-1]
      #Loop para que o usuario escolha o aluno para determinada posição mediante a variavel criada que percorre a lista de posição
      while True:
        pos = input(f"\nDiga quem ficou em {posicao} lugar: ")
        #Condição para que seja apenas aceitado quem está na lista em alunos
        if pos in alunos:
          #Codição para verificar se a posição já foi preenchida
          if posicaoAluno[position[i-1]] is None:
            posicaoAluno[position[i-1]] = pos
            print(f"\n{posicao} - {pos}\n")
          break
        else:
          print("\nAluno não encontrado, tente novamente\n")

#Apenas para mostrar como ficou o Ranking
def rankingPreenchido():
  print("\nRanking:\n")
  for posicao in position:
    print(f"{posicao} - {posicaoAluno[posicao]}\n")




while True:
  print("\nAções disponiveis:\n")
  print("\n1. Adicionar alunos\n")
  print("2. Lista de alunos\n")
  print("3. Ver Ranking\n")
  print("4. Determinar Ranking\n")
  print("5. Ranking Preenchido\n")
  print("6. Encerrar Sistema\n\n")
  escolha = int(input("Escolha a ação que deseja: "))

  if escolha == 1:
    print("")
    nomeAlunos()
    print("")
  elif escolha == 2:
    listaAlunos()
  elif escolha == 3:
    ranking()
    print("")
  elif escolha == 4:
    escolhaPosicao()
    print("")
  elif escolha == 5:
      rankingPreenchido()
      print("")
  elif escolha == 6:
    print("\n\nSistema encerrado. Até logo!")
    break
  else:
    print("Alternativa invalida, tente novamente")

  

  
'''

Ideias para o futuro:

- Adicionar um controle (Trazer um sistema que deixa o usuario escolher que quer fazer, se quer adicionar alunos, adicionar notas, etc) - [FEITO PARCIALMENTE]

- Adicionar objetividade (Notas/presença/desempenho) - 

- Adicionar motivação - Se em objetividades for algo negativo, adicionar mensagens personalizadas 

- Adicionar uma implementação que não limite o número de alunos para que caso não queira adicionar alunos, se encerre ali a solicitação - [FEITO]

- Adicionar uma implementação para adicionar alunos novos - [FEITO]

Implementações adicionadas sem serem previstas

º - Adicionado especificações para que o sistema informe questões especificas: Mensagem para lista vazia, mensagem para informar quantos alunos foram adicionados. 

º - Adicionado um controle na questão de determinar o ranking: Só poderá determinar a posição dos alunos se houver pelo menos 3 alunos.


'''
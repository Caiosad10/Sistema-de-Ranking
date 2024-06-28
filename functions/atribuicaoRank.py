import dados

#Função para determinar a posição dos alunos
def atribuicaoRank():

  if len(dados.alunos) == 0:
    print("\n\t\tLista de Alunos vazia! Impossivel determinar posições!")
  elif len(dados.alunos) < 3:
    print("\n\t\tQuantidade insuficiente de alunos para determinar as posições! Adicione mais alunos! (É necessario no minimo três(3) nomes para determinar o Ranking)")
  elif len(dados.notas) < len(dados.alunos):
    print("\n\t\tQuantidade insuficiente de notas para determinar as posições!")
  elif len(dados.alunos) >= 3 and len(dados.notas) == len(dados.alunos):
    dados.notasMaiorMenor = sorted(dados.notas, reverse=True)
    indicesMaiorMenor = sorted(range(len(dados.notas)), key=lambda k: dados.notas[k], reverse=True)
  #Loop para atribuir as 3 posições
    for i in range(3):
      dados.posicaoAluno[dados.position[i]] = dados.alunos[indicesMaiorMenor[i]]
      print(f"\n{dados.position[i]} -{dados.alunos[indicesMaiorMenor[i]]}\n") 

    if all(value is not None for value in dados.posicaoAluno.values()):
      print("\n\t\tPosições determinadas com sucesso!")
    else:
      print("\n\t\tErro ao determinar as posições!")


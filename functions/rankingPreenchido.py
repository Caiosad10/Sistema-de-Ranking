import dados

#Apenas para mostrar como ficou o Ranking
def rankingPreenchido():
  if len(dados.alunos) < 3:
    print("\n\t\tVocê precisa ter pelo menos 3 alunos, e depois determinar o Ranking para poder ve-lo preenchido! (Lembrando que é necessario determinar as notas dos alunos")
  elif len(dados.notasMaiorMenor) == 0:
    print("\n\t\tERROR! Parece que está faltando algo, caso não tenha adicionado as notas dos alunos, adicione! (Lembre-se de ir em 'Determinar' antes de ver o Ranking!)")
  elif len(dados.posicaoAluno) <3:
      print("\n\t\tVocê precisa determinar as posições antes de ver o Ranking! (Lembrando que é necessario no minimo 3 alunos para determinar o Ranking)")
  elif len(dados.alunos) >=3 and len(dados.notasMaiorMenor) == len(dados.alunos):
    print("\nRanking:\n")
    for i in range(3):
      print(f"{dados.position[i]} - {dados.posicaoAluno[dados.position[i]]}\t\tNota: {dados.notasMaiorMenor[i]}\n")
  else:
    print("\n\t\tErro ao determinar o Ranking!")
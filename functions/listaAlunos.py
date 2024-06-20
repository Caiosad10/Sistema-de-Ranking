import dados

def listaAlunos():
  print("\nLista de alunos:\n")
  if len(dados.alunos) == 0:
    print("\t\tLista vazia!\n\nNenhum aluno adicionado ainda!\n\n")
  for i, aluno in enumerate(dados.alunos):
    print(f"{i + 1} - {aluno}")


#OBSERVAÇÃO - VERIFICAR SE ESTÁ FUNCIONANDO
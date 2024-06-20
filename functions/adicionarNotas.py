import dados

def adicionarNotas():
  print("\n\t\tAdicionar notas dos alunos\n")

  while dados.iNotas < len(dados.alunos):
    nota = input(f"Digite a nota do {dados.alunos[dados.iNotas]} ou 's' para sair: ")
    if nota.lower() == "s":
      break
    else:
      try:
        nota = float(nota)
        dados.notas.append(nota)
        dados.iNotas += 1
      except ValueError:
        print("Digite um valor numerico para as notas!")

  '''print("\n\t\tAdicionar notas dos alunos\n")
  #Loop para adicionar as notas dos alunos
  for i in range(len(alunos)):
    nota = float(input(f"Digite a nota do aluno {alunos[i]}: "))
    notas.append(nota)'''

import dados

#Função para mostrar as posições disponiveis
def ranking():
  print("\nPosições:\n")
  for posicao in dados.position:
    print(f"{posicao} - ")
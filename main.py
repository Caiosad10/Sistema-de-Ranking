import time

from functions.nomeAlunos import nomeAlunos
from functions.listaAlunos import listaAlunos
from functions.ranking import ranking
from functions.adicionarNotas import adicionarNotas
from functions.atribuicaoRank import atribuicaoRank
from functions.rankingPreenchido import rankingPreenchido
import limpar


while True:
  limpar.limparConsole()
  print("\nAções disponiveis:\n")
  print("\n1. Adicionar alunos\n")
  print("2. Lista de alunos\n")
  print("3. Posições disponiveis\n")
  print("4. Adicionar notas dos alunos\n")
  print("5. Determinar Ranking\n")
  print("6. Ranking Preenchido\n")
  print("7. Encerrar Sistema\n\n")
  escolha = int(input("Escolha a ação que deseja: "))

  if escolha == 1:
    print("")
    limpar.limparConsole()
    nomeAlunos()
    time.sleep(3)
    
  elif escolha == 2:
    limpar.limparConsole()
    listaAlunos()
    time.sleep(3)
  elif escolha == 3:
    limpar.limparConsole()
    ranking()
    time.sleep(3)
    
  elif escolha == 4:
    limpar.limparConsole()
    adicionarNotas()
    time.sleep(3)
  elif escolha == 5:
    limpar.limparConsole()
    atribuicaoRank()
    time.sleep(3)
    
  elif escolha == 6:
      limpar.limparConsole()
      rankingPreenchido()
      time.sleep(3)
      
  elif escolha == 7:
    limpar.limparConsole()
    print("\n\nSistema encerrado. Até logo!")
    time.sleep(2)
    break
  else:
    print("Alternativa invalida, tente novamente")

  

  
'''

IDEIAS PARA O FUTURO:

- Adicionar um controle (Trazer um sistema que deixa o usuario escolher o que quer fazer, se quer adicionar alunos, notas e desempenho) - [FEITO PARCIALMENTE]

- Adicionar objetividade (Notas/presença/desempenho) - 

- Adicionar motivação - Se em objetividades for algo negativo, adicionar mensagens personalizadas 

- Adicionar uma implementação que não limite o número de alunos para que caso não queira adicionar alunos, se encerre ali a solicitação - [FEITO]

- Adicionar uma implementação para adicionar alunos novos - [FEITO]

- Adicionar transições para resultados da escolha, por exemplo para limpar a tela e deixar o usuario preenchendo os dados, depois de finalizar, limpa a tela e volta para o menu principal - [FEITO]

- Adicionar uma funcionalidade na qual uma opção só irá aparecer se o usuario executar outra função, por exemplo, a função "adicionar as notas" não irá aparecer nas escolhas se o usuario não adicionar os alunos (Pode ser vir para outras escolhas tambem para que seja otimizado o codigo)
 
- Adicionar Materias (Para contexto escolar)

IMPLEMENTAÇÕES JÁ ADICIONADAS SEM SEREM PREVISTAS

º - Adicionado especificações para que o sistema informe questões especificas, como por exemplo: Mensagem para lista vazia; Mensagem para informar quantos alunos foram adicionados e etc. 

º - Adicionado um controle na questão de determinar o ranking: Só poderá determinar a posição dos alunos se houver pelo menos 3 alunos. (MODIFICAÇÃO - Alem de ter os alunos, é necessario nota tambem) 

º - Adicionado a logica de que em atribuição de notas, caso o usuario sair e deixar de atribuir a nota dos alunos restantes, posteriormente ele poderá dar continuidade de onde parou.

ERROS 

- Erro em adicionar nota de alunos: 

  Caso o usuario digite "s" para sair, ele não sai e já pula para o proximo aluno; - [RESOLVIDO]
  
  Caso o usuario não insira um valor numerico, ele avisa que só pode inserir um valor numerico e pula para o proximo aluno - [RESOLVIDO]

- Erro em determinar o ranking:

  Caso o usuario selecionar, pode dar algum erro e quebrar o codigo. E ainda assim indica que a atribuição foi feita com sucesso. - [RESOLVIDO]
  
'''
import random #usado para importar comando de sorteio
p1, p2, p3, p4, p5, p6, p7, p8, p9 = '1', '2', '3', '4', '5', '6', '7', '8', '9' #variaveis do tabuleiro

jogador_da_vez = '' #define se X ou O está jogando

quantidade_de_jogadas = 0 #contador de jogadas para verfificar se deu velha

def ganhar(p1, p2, p3, p4, p5, p6, p7, p8, p9): #funcao para verificar quando tem uma diagonal, fila ou coluna com X ou O, assim, temos um ganhador
  global jogador_da_vez #define X ou O como variavel para todo o programa
  if (p1 == jogador_da_vez and p2 == jogador_da_vez and p3 == jogador_da_vez) or \
     (p4 == jogador_da_vez and p5 == jogador_da_vez and p6 == jogador_da_vez) or \
     (p7 == jogador_da_vez and p8 == jogador_da_vez and p9 == jogador_da_vez) or \
     (p1 == jogador_da_vez and p4 == jogador_da_vez and p7 == jogador_da_vez) or \
     (p2 == jogador_da_vez and p5 == jogador_da_vez and p8 == jogador_da_vez) or \
     (p3 == jogador_da_vez and p6 == jogador_da_vez and p9 == jogador_da_vez) or \
     (p1 == jogador_da_vez and p5 == jogador_da_vez and p9 == jogador_da_vez) or \
     (p3 == jogador_da_vez and p5 == jogador_da_vez and p7 == jogador_da_vez):
    return True
  return False

def tabuleiro(): #funcao que tem como objetivo printar o tabuleiro toda vez que uma jogada é feita
    global p1, p2, p3, p4, p5, p6, p7, p8, p9 
    print (p1 + '|' + p2 + '|' + p3)
    print ('_____________')
    print (p4 + '|' + p5 + '|' + p6)
    print ('_____________')
    print (p7 + '|' + p8 + '|' + p9)

def jogar(jogador_da_vez,posicao): #funcao usada para gerar a sua jogada no tabuleiro, ou seja, se voce digitar que a sua jogada é igual a 2, a função vai verificar se voce é X ou O e vai substituir na posição 2(p2) do tabuleiro
    global p1, p2, p3, p4, p5, p6, p7, p8, p9 
    global quantidade_de_jogadas 
    quantidade_de_jogadas = quantidade_de_jogadas + 1 #no contador de jogadas, acrecenta-se um +1 para cada jogada feita, assim, terá um controle de quantas jogadas já foram executadas para verificar velha
    if posicao == 1:
        p1 = jogador_da_vez
    if posicao == 2:
        p2 = jogador_da_vez
    if posicao == 3:
        p3 = jogador_da_vez
    if posicao == 4:
        p4 = jogador_da_vez
    if posicao == 5:
        p5 = jogador_da_vez
    if posicao == 6:
        p6 = jogador_da_vez
    if posicao == 7:
        p7 = jogador_da_vez
    if posicao == 8:
        p8 = jogador_da_vez
    if posicao == 9:
        p9 = jogador_da_vez

def verificar_velha(): #funcao que verifica se já foram feitas 9 jogadas e não tiveram ganhadores. Então, retornará True para a velha
  global quantidade_de_jogadas
  if quantidade_de_jogadas >=9 and not ganhar(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    return True
  return False

def jogar_novamente(): #quando o jogo for concluido, a funcao jogar_novamente vai pedir para o usuario se ele deseja jogar novamente ou sair
    decisao = int(input('Insira 1 para jogar novamente ou 2 para sair: '))
    while (decisao): 
        if decisao == 1: #enquanto a decisao for jogar novamente, a funcao que engloba todo o jogo será chamada e repetida
            jogo()
        elif decisao == 2: #enquanto a decisao for sair, a funcao irá printar espero que tenha gostado!
            print ('espero que tenha gostado!')
            break
        else: #e se o usuario digitar um numero que não está listado no input, ele vai printar que o comando não existe
            print ('este comando não existe')
            break #o break está sendo usado para parar de printar infinitamente a mensagem do comando else


def verificar_jogada(j): #esta funcao é usada para verificar se a posição que o usuario deseja jogar esta válida, ou seja, não tem X ou O ocupando o seu lugar. Se a posicao estiver ocupada, o comando para inserir sua jogada vai se repetir até que o usuario digite uma jogada que seja válida
    if j == 1: 
        if p1 == '1':
            return True
        else:
            return False
    if j == 2:
        if p2 == '2':
            return True
        else:
            return False
    if j == 3:
        if p3 == '3':
            return True
        else:
            return False
    if j == 4:
        if p4 == '4':
            return True
        else:
            return False
    if j == 5:
        if p5 == '5':
            return True
        else:
            return False
    if j == 6:
        if p6 == '6':
            return True
        else:
            return False
    if j == 7:
        if p7 == '7':
            return True
        else:
            return False
    if j == 8:
        if p8 == '8':
            return True
        else:
            return False
    if j == 9:
         if p9 == '9':
            return True
         else:
            return False
    else:
        return False

def resetar_tabuleiro(): #esta funcao vai fazer uma atualizaçao do tabuleiro apos as jogada do usuario
  global quantidade_de_jogadas, p1, p2, p3, p4, p5, p6, p7, p8, p9 
  p1, p2, p3, p4, p5, p6, p7, p8, p9 = '1', '2', '3', '4', '5', '6', '7', '8', '9'
  quantidade_de_jogadas = 0 

def jogo(): #funcao responsavel por tudo o que acontece dentro do jogo
  global jogador_da_vez 
  jogador_da_vez = ""
  jogada = '1', '2', '3', '4', '5', '6', '7', '8', '9'
  resetar_tabuleiro()

  adversario = int(input('Insira 1 para jogar contra um amigo ou 2 para jogar contra o computador: ')) #esse input é o começo do jogo e tem como finalidade verificar se o usuario quer jogar contra um amigo ou contra o computador
  if adversario == 1:
      
      jogando = True 

      j1 = input('Jogador x, digite seu nome: ') #se o usuario digitar que quer jogar contra um amigo, o programa pedirá o nome de seus respectivos jogadores como X e O
      j2 = input('Jogador o, digite seu nome: ')
      sorte = random.randint(1,3) #comando para sortear se o jogador a começar a jogar é o X ou a O
      if sorte == 1:
          print ('jogador começa')
          jogador_da_vez = 'x'
      else:
          print ('jogador o começa')
          jogador_da_vez = 'o'
          
      ganhador = False
      while(jogando and not ganhador and not verificar_velha()): #Indica uma repetição que será feita enquanto jogando for igual a True e verificar velha e ganhador retornarem False
          
                
               
          tabuleiro()#Aqui chamamos a função para printar o tabuleiro
      
          jogada = 45#É um exemplo que se a jogada for maior que 9 ele não será válida pois não tem no tabuleiro
          print (' eh a vez de: ' + jogador_da_vez)
          while not verificar_jogada(jogada):#Compara se veridicar jogada retornar False, entrará na função com parametro jogada 
              jogada = int(input('Insira sua jogada: '))#O jogador irá escolher sua jogada 

          jogar(jogador_da_vez,jogada)#Chamamos a função jogar, com os paramentros jogador da vez e jogada 
          ganhador = ganhar(p1, p2, p3, p4, p5, p6, p7, p8, p9)
          if jogador_da_vez == 'x':
              jogador_da_vez = 'o'
          else:
              jogador_da_vez = 'x'

      if verificar_velha():
        print ('Deu velha!')
      elif jogador_da_vez == 'x':
        print ('o ganhador foi: o')
      elif jogador_da_vez == 'o':
        print ('o ganhador foi: x')
      

      jogar_novamente()#Chama a função jogar novamente, para saber se o jogador deseja continuar jogando 
          

              
  elif adversario == 2:
        jogando = True
        jogada_pc = ''

        ganhador = False#Define ganhador como False

        while(jogando and not ganhador and not verificar_velha()):#Indica uma repetição que será feita enquanto jogando for igual a True e verificar velha e ganhador retornarem False

            jogador_da_vez = 'x'
            tabuleiro()
            while not verificar_jogada(jogada):#Esta repetição será feita quando verificar jogada retornar False
                jogada = int(input('Insira a sua jogada como jogador x: '))
            jogar(jogador_da_vez, jogada)
            ganhador = ganhar(p1, p2, p3, p4, p5, p6, p7, p8, p9)
            jogador_da_vez = 'x'

            if not ganhador:
              while not verificar_jogada(jogada_pc):
                  jogada_pc = int(random.randrange(1, 10))
              jogador_da_vez = 'o'
              jogar(jogador_da_vez, jogada_pc)
              ganhador = ganhar(p1, p2, p3, p4, p5, p6, p7, p8, p9)
              jogada_pc = jogador_da_vez

        if verificar_velha():
            print('Deu velha!')
        elif jogador_da_vez == 'x':
            print('o ganhador foi: x')
        elif jogador_da_vez == 'o':
            print('o ganhador foi: o')

        jogar_novamente()
          
      
  else:
      print ('este comando é invalido')
      
jogo()

    


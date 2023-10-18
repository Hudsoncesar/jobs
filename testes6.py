#class Lista():
    #lista = []
    #tamanho = 0

    #def inserirItens(self, quantidade):
       # msg = "Insira um item na lista"
        #for i in range(quantidade):
            #self.lista.append(msg)
           # self.tamanho += 1




#class cachorro():
    #def __int__(self,nome,nascimento):
        #self.nome = str(nome)
        #self.nascimento = str(nascimento)

#def funçaocachorro():
   # menu = ''

 #   while menu != '6':
    #    menu = input("[1] latir\n[2] comer\n[3] objeto do cachorro\n[4] Encerrar\n\nQual opção você deseja?\n")
     #   if menu == '1':
      #      print("\no cachorro latiu\n")
       # elif menu == '2':
        #    print("\no cachorro comeu\n")
        #elif menu == '3':
         #   print("\nurso\n")
        #else:
         #   print("\no cachorro saiu do chat\n")
          #  break 
#lista = [20, 30, 40, 50, 60] 
#H = sum(lista)
#print(H)



class profissional:
  def _int_(self,idade,cidade,estado,salário,escolaridade):
    self.idade = idade
    self.cidade = cidade
    self.estado = estado
    self.salário = salário
    self.escolaridade = escolaridade
    
    def resposta():
      formulario = ''


      while formulario != '6':
            formulario = ("[1] idade\n[2] cidade\n[3] estado\n[4] sálario\n[5] escolaridade\n[6] sair\n \nselecione uma pergunta\n ")
        if formulario == '1':
          x= input("qual sua idade?")
          print(x)
        elif formulario =='2':
          a = input("qual a sua cidade?")
          print(a)
        elif formulario =='3':
          b= input("qual o seu estado?")
          print(b)
         elif formulario =='4':
          c = input("qual seu sálario?")
          print(c)
        elif formulario =='5':
          d = input("qual a sua escolaridade?")
          print(d)
        else:
          print("\n muito obrigado")
          break        
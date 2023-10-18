#class Lista():
    #lista = []
    #tamanho = 0

    #def inserirItens(self, quantidade):
       # msg = "Insira um item na lista"
        #for i in range(quantidade):
            #self.lista.append(msg)
           # self.tamanho += 1




class cachorro():
    def __int__(self,nome,nascimento):
        self.nome = str(nome)
        self.nascimento = str(nascimento)

def funçaocachorro():
    menu = ''

    while menu != '6':
        menu = input("[1] latir\n[2] comer\n[3] objeto do cachorro\n[4] Encerrar\n\nQual opção você deseja?\n")
        if menu == '1':
            print("\no cachorro latiu\n")
        elif menu == '2':
            print("\no cachorro comeu\n")
        elif menu == '3':
            print("\nurso\n")
        else:
            print("\no cachorro saiu do chat\n")
            break 
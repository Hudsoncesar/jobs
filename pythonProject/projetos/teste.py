letras = ("e", "t", "p", "s")
listC = ["e5_t10_p8_s8", "e10_t7_p7_s8", "e8_t5_p4_s9", "e2_t2_p2_s1", "e10_t10_p8_s9"]
listY = []



def arrumar():
    for j in range(len(listC)):
        nLista = listC[j].split("_")

        listYD = {}


        for i in range(len(nLista)):
            valor = int(nLista[i][1:])
            listYD[letras[i]] = valor
        listY.append(listYD)


def minimo():
    x = {} 
    
    for i in range(len(letras)):
        y = int(input(f'Digite o valor minimo da nota "{letras[i]}":'))
        x[letras[i]] = y

    print("\n")

    for i in range(len(listY)):
        status = 0

        for j in range(len(letras)):
            if listY[i][letras[j]] >= x[letras[j]]:
                status = status + 1
        if status == 4:
            print(f"Candidato {i + 1} foi aprovado.")

    print("\nSe nada for informado, nenhum candidato foi aprovado")


arrumar()
minimo()



repeticoes = int(input())

contagem = 6                ##contador 2º while
cont = 0                    ##contador 1º while
localMaiorRep = [0,0,0]     #contagem de qual linha é a mais usada
regioes = [0,0,0]           #primeiro indice é linha 1 e 2
                            #segundo indice é linha 3 e 4
                            #Tercerio indice é linha 5 e 6


while cont != repeticoes:
    localMaiorRep = [0,0,0]     #contagem de qual linha é a mais usada
    listEntrada = []

    while contagem > 0:         ###Entradas das 6 linhas
        entrada = input()
        listEntrada.append(entrada.split(sep = " "))
        contagem = contagem - 1
        
    linha = 0
    localMaiorRep = [0,0,0]     #lista das linhas + usadas
    
    for x in listEntrada:
        soma = 0
        for j in x:
            soma = soma + int(j)

        if linha < 2:
            localMaiorRep[0] += soma
        else:
            if linha < 4:
                localMaiorRep[1] += soma
            else:
                if linha < 6:
                    localMaiorRep[2] += soma

        linha += 1
 
    contagem = 6        # reset da contagem de linha
    cont = cont + 1     #proximo conjunto de numeros
    
    maior = max(localMaiorRep)
    final = localMaiorRep.index(maior)
    regioes[final] += 1

print(localMaiorRep)
print(regioes)

maior = max(regioes)
final = regioes.index(maior)

if final == 2:
    print("inferior")
else:
    if final == 1:
        print("meio")
    else:
        if final == 0:
            print("superior")
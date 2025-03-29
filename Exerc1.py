repeticoes = int(input())

contagem = 6  ##contador 2º while
cont = 0  ##contador 1º while
listEntrada = []
localMaiorRep = [0,0,0]

while cont != repeticoes:
    
    while contagem > 0:
        
        entrada = input()
        listEntrada.append(entrada.split(sep = " "))
        
        contagem = contagem - 1
        
    soma = 0
    linha = 0
    
    for x in listEntrada:
        soma = 0
        linha += 1
        for j in listEntrada:
            
            soma = 0
            soma = soma + j

        if linha <= 6:
            if linha <= 4:
                if linha <= 2:
                    
                    localMaiorRep[0] += 1
                localMaiorRep[1] += 1
            localMaiorRep[2] += 1
                
    

    
   # listEntrada = []
    contagem = 6
    cont = cont + 1
    
for x in listEntrada:
    
    print(x)
    
    
  #      cont2 = 0, max = 0
  #  
   ## for i in listEntrada:
        
  #      max += i[cont2]
   #     cont2 += 1
lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [2,2,1,1,4,4,5,5,6,7],
    [1,1,2,2,3,3,4,4,10,8],
    [10,9,8,7,6,5,4,3,2,1],
    [2,4,6,8,10,8,6,4,2,1],
    [1,3,5,7,9,10,1,2,3,4],
    [1,2,3,4,5,5,4,3,2,1],
    [2,1,3,2,4,3,5,4,6,5],
    [10,9,5,6,7,8,4,3,2,1],
    [9,9,9,9,9,8,8,8,7,7]
]

def encontra_primeiro_duplicado(lista_de_inteiros):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    
    for numero in lista_de_inteiros:
        if numero in numeros_checados:
            primeiro_duplicado = numero
            break
        
        numeros_checados.add(numero)
        

    print()
    print()
    return primeiro_duplicado

for lista in lista_de_listas_de_inteiros:
    print(lista,encontra_primeiro_duplicado(lista))
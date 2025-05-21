import os
os.system('cls')


lista = []

while True:

    print("Selecione uma opção")
    resposta = input("[i]nserir [a]pagar [l]istar: ")

    if resposta == "a":
        os.system('cls')
        i = int(input("Digite o número do índice do item que deseja apagar: "))
        
        lista.pop(i)
            
        indice = range(len(lista))
        for c in indice:
            print(c, lista[c])
        
    elif resposta == 'i':
        os.system('cls')
        a = input("Digite o item que deseja inserir: ")
        
        lista.append(a)

        indice = range(len(lista))
        for c in indice:
            print(c, lista[c])

    elif resposta == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada para listar!')

        indice = range(len(lista))
        for c in indice:
            print(c, lista[c])

    else:
        os.system('cls')
        print('Você não digitou nenhum dos valores aceitos!')
    


        
            

            
import os

os.system('cls')
palavra = input("Digite a palvra/frase oculta: ")
os.system('cls')
letra_certa = ""
tentativas = 0
letra_utilizada = set()

while True:
    letra = input("Digite uma letra: ")
    tentativas += 1

    if len(letra) > 1:
        print("Digite apenas uma letra")
        continue

    if letra in letra_utilizada:
            print("Essa letra já foi utilizada!")
            print(" ".join(sorted(letra_utilizada)))
            continue
    
    letra_utilizada.add(letra)

    if letra in palavra:
        letra_certa += letra
    
    palavraFormada = ''
    for letra in palavra:
        if letra in letra_certa:
            palavraFormada += letra

        else:
            palavraFormada += "*"

    os.system("cls")
    print("Palavra formada: ", palavraFormada)
    print("Letras já utilizadas: ", " ".join(sorted(letra_utilizada)))

    if palavraFormada == palavra:
        os.system("cls")
        print("Você Ganhou!")
        print("A palavra era: ", palavra)
        print("Tentativas: ", tentativas)
        break
    
    

    

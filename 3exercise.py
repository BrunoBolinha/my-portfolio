"""
Exercício 1


numero = input('Digite um número inteiro: ') 

if numero.isdigit():
    numero_int = int(numero)
    par_impar = numero_int % 2 == 0
    texto = "impar"

    if par_impar is True:
        texto = "par"

        print(f"{numero_int} é um número {texto}")

    else:
        print(f"{numero_int} é um número {texto}")

else:
    print("Você não digitou um número inteiro")


Exercício 2

hora = input('Olá, que horas são? ')
hora_int = int(hora)

if hora_int < 12 and hora_int > 0:
    print(f"Bom dia {hora_int}")

if hora_int < 18 and hora_int > 11:
    print(f"Boa tarde {hora_int}")

if hora_int < 25 and hora_int > 17:
    print(f"Boa noite {hora_int}")

if hora_int > 24:
    print("Você não digiticou nenhum valor condizente com o horário")

Exercício 3
"""

nome = input("Digite seu nome: ")

tamanho = len(nome)

if tamanho < 5:
    print("Seu nome é curto")    

if tamanho < 7 and tamanho > 4:
    print("Seu nome é normal") 

if tamanho > 6:
    print("Seu nome é grande") 

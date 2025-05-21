nome = input("Digite seu nome: ")

i=0
nomecorrigido=""

while i < len(nome):

    nomequebrado = nome[i]
    nomecorrigido += f'*{nomequebrado}'
    i += 1
   
print(nomecorrigido)
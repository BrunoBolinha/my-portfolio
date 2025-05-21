
perguntas = [

    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '2', '3', '4'],
        'Resposta': '4',
    },

    {
        'Pergunta': 'Quanto é 5+5',
        'Opções': ['10', '20', '30', '40'],
        'Resposta': '10',
    },

    {
        'Pergunta': 'Quanto é 10+10',
        'Opções': ['10', '20', '30', '40'],
        'Resposta': '20',
    }

]

acertos = 0

for pergunta in perguntas:

    print('Pergunta:', pergunta['Pergunta'])
    print()
    
    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    resposta = input('Escolha uma opção: ')

    acertou = False
    resposta_int = None
    qtd_opcoes = len(opcoes)

    if resposta.isdigit():
        resposta_int = int(resposta)
    
    if resposta_int is not None:
        if resposta_int >= 0 and resposta_int < qtd_opcoes:
            if opcoes[resposta_int] == pergunta['Resposta']:
                acertou = True
    
    if acertou:
        print('Acertou')
        acertos += 1
    else:
        print('Errou')


print('Você acertou: ', acertos)
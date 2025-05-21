import os
import json

#################### Funções ####################

def listar(tarefas):
    os.system('cls')
    print()
    if not tarefas:
        print("nenhuma tarefa para listar")
        return
    
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'\t{tarefa}')

def desfazer(tarefas, tarefas_refazer):
    os.system('cls')
    print()
    if not tarefas:
        print("nenhuma tarefa para desfazer")
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    os.system('cls')    
    print()
    if not tarefas:
        print("nenhuma tarefa para refazer")
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    os.system('cls')
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print("Você não digitou uma tarefa")
        return
    tarefas.append(tarefa)

def ler(tarefas, caminho_arquivo):
    dados = tarefas
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivos:
            dados = json.load(arquivos)
    except FileNotFoundError:
        print('Arquivo não existe')
        salvar(tarefas, caminho_arquivo)
    return dados

def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivos:
        dados = json.dump(tarefas, arquivos, indent=2, ensure_ascii=False)
    return dados

def sair(tarefas):
    print()
    for i in tarefas:
        if not tarefas:
            print('Programa encerrado.')
            break


#################### Estrutura ####################

CAMINHO_ARQUIVO = 'todo_list2.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'cls': lambda: os.system('cls'),
        'adicionar': lambda: adicionar(tarefa, tarefas),
        'sair': lambda: sair(tarefa)
    }

    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
        comandos['adicionar']
    comando()
    salvar(tarefas, CAMINHO_ARQUIVO)

    if tarefa == 'sair':
        print('Programa encerrado')
        break


"""
while True:

    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    else:
        adicionar(tarefa, tarefas)
        continue

"""

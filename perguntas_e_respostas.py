import time

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quantos dias tem um ano bissexto?',
        'respostas': {
            'a': '364',
            'b': '365',
            'c': '366',
            'd': '367',
        },
        'correto': 'c',
    },
    'Pergunta 2': {
        'pergunta': 'Quantas patas tem um inseto?',
        'respostas': {
            'a': '4',
            'b': '6',
            'c': '8',
            'd': '10',
        },
        'correto': 'b',
    },
    'Pergunta 3': {
        'pergunta': 'Quantas corcovas tem um camelo?',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'correto': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quantas corcovas tem um dromedário?',
        'respostas': {
            'a': '1',
            'b': '2',
            'c': '3',
            'd': '4',
        },
        'correto': 'a',
    },
}

acertos = 0
erros = 0

for rodada, valores in perguntas.items():
    print(f'\n{rodada}')
    time.sleep(1)
    print(valores['pergunta'])
    time.sleep(1)
    for alternativa, valor in valores['respostas'].items():
        print(f'{alternativa}: {valor}')
        time.sleep(0.5)
    resposta = input('Insira a resposta: ')
    correto = valores['correto']
    if resposta == correto:
        print('\nA sua resposta está correta')
        acertos += 1
    else:
        print('\nQue pena, vc errou')
        print(f'A resposta certa é {valores["respostas"][correto]}')
        erros += 1
    time.sleep(2)
print(f'\n{"*" * 8} Fim de jogo {"*" * 8}\n')
print(f'Vc acertou {acertos} e errou {erros}')
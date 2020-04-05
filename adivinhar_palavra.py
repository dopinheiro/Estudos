segredo = 'perfume'
digitadas = []
tentativas = 3
print('Segredo: ', len(segredo) * '*')


while True:
    if tentativas > 0:
        letra = input('\nDigite uma letra: ')

        if len(letra) > 1:
            print('Digite apenas UMA letra...')
            continue

        if letra in segredo:
            print('A palavra contém essa letra')
            digitadas.append(letra)
        else:
            print('Que pena, tente de novo')
            tentativas -= 1
            print(f'Vc tem mais {tentativas} tentativas.')
        segredo_temporario = ''
        for caractere in segredo:
            if caractere in digitadas:
                segredo_temporario += caractere
            else:
                segredo_temporario += '*'
        print('\nPalavra secreta:', segredo_temporario)
        if segredo_temporario == segredo:
            print('Parabéns, vc ganhou!!!')
            break
    else:
        print('Vc excedeu a quantidade de tentativas')
        break
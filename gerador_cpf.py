from random import randint


def gera_cpf():
    cpf_str = ''
    for numero in range(9):
        cpf_str = cpf_str + str(randint(0,9))

    soma = 0
    for indice, multiplicador in enumerate(range(10, 1, -1)):
        soma += int(cpf_str[indice]) * multiplicador
    temporario = 11 -soma%11
    primeiro = 0 if temporario > 9 else temporario

    soma = 0
    cpf_temp = cpf_str[:10] + str(primeiro)
    for indice , multiplicador in enumerate(range(11,1,-1)):
        soma += int(cpf_temp[indice]) * multiplicador
    temporario = 11 - soma % 11
    segundo = 0 if temporario > 9 else temporario
    verificador = str(primeiro) + str(segundo)
    return cpf_str + verificador


cpf = gera_cpf()
if not cpf.isnumeric():
    print('Insira o CPF sem pontos ou caracters especiais.')
else:
    new_cpf = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}'
    print(f'Um CPF válido foi gerado: {new_cpf}')

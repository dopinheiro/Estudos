def valida_cpf(cpf_str):
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
    return verificador


while True:
    cpf = input('Insira o seu CPF: ')
    if not cpf.isnumeric():
        print('Insira o CPF sem pontos ou caracters especiais.')
        continue
    else:
        verificador = valida_cpf(cpf)
        print('CPF válido' if verificador == cpf[-2:] else 'CPF inválido')
        break

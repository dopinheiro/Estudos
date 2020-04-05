def primeiro_digito(cpf_str):
    soma = 0
    for indice, multiplicador in enumerate(range(10, 1, -1)):
        soma += int(cpf_str[indice]) * multiplicador
    temporario = 11 -soma%11
    primeiro = 0 if temporario > 9 else temporario
    return primeiro 


def segundo_digito(cpf_str, verificador):
    soma = 0
    cpf_temp = cpf_str[:10] + str(verificador)
    for indice , multiplicador in enumerate(range(11,1,-1)):
        soma += int(cpf_temp[indice]) * multiplicador
    temporario = 11 - soma % 11
    segundo = 0 if temporario > 9 else temporario
    return segundo

while True:
    cpf = input('Insira o seu CPF: ')
    if not cpf.isnumeric():
        print('Insira o CPF sem pontos ou caracters especiais.')
        continue
    else:
        primeiro = primeiro_digito(cpf)
        segundo = segundo_digito(cpf, primeiro)
        resultado = str(primeiro) + str(segundo)
        print('CPF válido' if resultado == cpf[-2:] else 'CPF inválido')
        break
primeiro_valor = int(input('Digite um valor qualquer: '))
segundo_valor = int(input('Digite outro valor qualquer: '))

if primeiro_valor > segundo_valor:
    print(f'O número {primeiro_valor} é maior que o número {segundo_valor},')
elif segundo_valor > primeiro_valor:
    print(f'O número {segundo_valor} é maior que o número {primeiro_valor},')
else:
    print(f'O número {primeiro_valor} é igual ao número {segundo_valor},')

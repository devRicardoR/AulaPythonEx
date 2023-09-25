"""
Peça para o usuário digitar o seu nome.
Peça para o usuário digitar a sua idade.
Se o nome e a idade forem digitados:
Imprima:
O seu nome é:
Você tem tantos anos:
O seu nome invertido é:
O seu nome tem x letras: ('Sempre lembrar que o python vai contar os espacos se tiver no nome')
A ultima leatra do seu nome é:
A primeira letra do seu nome é:

"""
nome = str(input('Digite o seu nome: '))
idade = int(input('Agora digite a sua idade: '))
if nome and idade:
    print(f'O seu nome é: {nome},')
    print(f'A sua idade é: {idade}, ')
    print(f'O seu nome invertido é: {nome[::-1]}, ')
        print(f'O seu nome tem {len(nome)} letras.')
        print(f'A última letra do seu nome é: {nome[-1]}')
        print(f'A primeira letra do seu nome é: {nome[0]}')
    else:
    print('Erro! Você deixou um dos campos em branco! ')
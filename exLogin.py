"""
Desenvolva um algoritmo, que peça para o usuário digitar a letra "E" para entrar no sistema, e uma senha.
Senha válida: 12345. Imprimir: Seja bem vindo ao sistema, ou "Erro! Acesso ao sistema inválido."

"""
entrada_usuario = str(input('Digite a letra "E" para entrar no sistema: '))
senha_usuario = int(input('Digite a sua senha: '))
senha_valida = 12345

if entrada_usuario == "E" and (senha_usuario == senha_valida):
    print('Seja bem vindo(a) ao sistema! ')
else:
    print('Erro! Acesso inválido! ')

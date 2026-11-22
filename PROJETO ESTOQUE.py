estoque = 0
menu = '''
====== ESTOQUE ======
[1] Adicionar produto
[2] Retirar produto
[3] Ver estoque
[4] Sair
====================>'''

while True:
    opcoes = input(menu)

    if opcoes == '1':
        adicionar = int(input('Quantos produtos deseja adicionar: '))
        estoque += adicionar

    elif opcoes == '2':
        retirar = int(input('Quantos produtos deseja retirar: '))
        if retirar <=0:
            print('Operação Recusada')
        elif retirar > estoque:
            print('Não há produtos suficientes em estoque.')
        else:
            estoque -= retirar

    elif opcoes == '3':
        print(f'Estoque atual: {estoque} produtos')

    elif opcoes == '4':
        print('Finalizando o Programa...')
        break

    else:
        print('Selecione uma opção válida!')
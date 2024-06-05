deposito = 0
saque = 0
extratos = []
cont_saques = 0


while True:

    opção = int(input(' 1-Deposito; 2-Saque; 3-Extrato; 4-Sair; '))
    print('')
    if opção == 1:

        depositar = float(input('Valor para depositar: '))
        if depositar < 0:
            print('Valor inválido! Valor negativo inserido')
        else:
            deposito += depositar
            print(f'Valor depositado: R${depositar:.2f}')
            extratos.append(f'Deposito: R$ {depositar:.2f}')

        print('')

    if opção == 2:
        if cont_saques == 3:
            print('Limite diário alcançado')
            continue
        valor_sacado = float(input('Valor a sacar: '))
        if valor_sacado > 500:
            print('Valor inválido! Valor máximo ultrapassado')
        elif valor_sacado < 0:
            print('Valor inválido! Valor negativo inserido')
        else:
            print(f'Valor sacado de: R${valor_sacado:.2f}')
            deposito -= valor_sacado
            print(f'Saldo atual: R${deposito:.2f}')
            cont_saques += 1
            extratos.append(f'SaqueDeposito: R$ {valor_sacado:.2f}')

        print('')

    if opção == 3:
        print('=========Extratos========')
        for transação in extratos:
            print(transação)

    if opção == 4:
        print('Obrigado pela preferência! ')
        break

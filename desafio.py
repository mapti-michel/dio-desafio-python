menu = """

[d] Depositar
[s] Sacar (Limite R$ 500,00)
[e] Extrato
[q] Sair


=> """

valor = 0.0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("A operação falhou. O valor informado é inválido")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        numero_saques += 1

        if excedeu_saldo:
            print("Operação falhou ! Você não tem saldo para esta transação.")
        elif excedeu_limite:
            print("Operação falhou ! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou ! Você excedeu o número máximo de mensagens.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
        else:
            print("Operação falhou ! O valor informado é inválido.")

    elif opcao == "e":
        print("\n============= EXTRATO =============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n===================================")

    elif opcao == "q":
        print("O banco DIO agradece a sua visita.")
        break
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")





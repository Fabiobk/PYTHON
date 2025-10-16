saldo = 0 
saque_realizados = 0
limite_saque = 3
limite=500
while True:
    opcao = input("""
  
  [d] - Deposito
  [s] - Saque
  [e] - Extrato
  [q] - Sair
  """).lower()def

    if opcao == 'd':
        valor = float(input("informe valor do deposito")) 
        if valor < 0:
            print("Valor invalido")
        else:
            saldo += valor

    elif opcao == 's':
        valor = float(input("informe valor do saque"))

        if valor < saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print(f"Limite de saque e {limire:.2f}")
        elif saque_realizados > limite_saque:
            print("Limite de saque atingido ")
        elif valor <= 0:
            print("valor invalido pra saque")
        else:
            saldo -= Valor

    elif opcao == 'e':
        print("==== EXTRATO=======")
        print(f"seu saldo atual ={valor:.2f}")

    elif opcao == 'q':
        print("saindo do sistema")
        break
d
               
saldo = 0 
saque_realizados = 0
limite_saque =3
limite=500
valor=0
def deposito(saldo):

        valor = float (input("informe valor do deposito")) 
        if valor < 0:
            print("Valor invalido")
        else:
          saldo += valor
          return saldo
        
def extrato (saldo):
    print("==== EXTRATO=======")
    print(f"seu saldo atual ={saldo:.2f}")

def saque(saldo, saque_realizados, limite_saque, limite):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0:
        print("Valor inválido.")

    elif valor > saldo:
        print("Saldo insuficiente.")

    elif valor > limite:
        print(f"Limite por saque é R$ {limite:.2f}")

    elif saque_realizados >= limite_saque:
        print("Limite diário de saques atingido")

    else:
        saldo -= valor
        saque_realizados += 1
        print("Saque realizado com sucesso!")

    return saldo, saque_realizados

        
        
while True:
    opcao = input("""
  
  [d] - Deposito
  [s] - Saque
  [e] - Extrato
  [q] - Sair
  """).lower()

    if opcao == 'd':
        
        saldo = deposito (saldo)

    elif opcao == 's':
      saldo, saque_realizados = saque(saldo, saque_realizados, limite_saque, limite)


    elif opcao == 'e':
           extrato(saldo)

    elif opcao == 'q':
        print("saindo do sistema")
        break
    

   
    
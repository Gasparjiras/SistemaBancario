menu = """
    
[d] Depositar
[e] Extrato
[s] Sacar
[q] Sair


 =>    """

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito :R$ {valor:.2f}\n"


    elif opcao == "s":
        valor = float(input("Digite o valor que deseja sacar :"))
        
        exercedeu_valor = valor > saldo
        exerxedeu_limite = valor > limite
        exercedeu_saques = numero_saques >= LIMITE_SAQUES

        if exercedeu_valor :
            print("Operação falhou! Você não tem saldo suficiete")


        elif exerxedeu_limite :
             print("Operação falhou! Você exercedeu o limite de 500.00 R$ ")
             
        elif exercedeu_saques :
            print("Operação falhou! Você exercedeu o limites de saques")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque :R$ {valor:.2f}\n"
            numero_saques +=1

        else :
            print("Operação falhou! o valor informado é inválido.")




    elif opcao =="e":
        print("\n=============Extrato============")
        print("Não foram realizadas movimentaçoes." if not extrato else extrato)
        print(f"\nSaldo : R$ {saldo:.2f}")
        print("==================================")

    elif opcao =="q":
        break
    else:
        print("Operação invalida. por favor selecione  novamente  a operação desejada")


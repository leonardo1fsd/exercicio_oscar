
conta_corrente = 10000.00
poupanca = 1500.00
for i in range(7):
  email = input("digite seu email: ")
  senha = input( "digite sua senha: ")

  print(type(email))
  print(type(senha))

  if (email =="leo" and senha == "1234"):
    print("acesso permitido")
    opcao = input("----CONTA BANCARIA----\n1- Saque \n2- deposito \n3- tranferencia \n4-saldo: \n")
    match opcao: 
       
      case "1":
         op = int(input("escolha entre: \n1- poupança \n2- conta corrente \n"))
         if(op == 1):
            saque = float(input("informe o valor do saque:\n"))
            poupanca= poupanca-saque
            print (" o saldo da poupança atualmente é: " + str(poupanca))
            
         if(op == 2):
            tranferencia = float(input("informe o valor da tranferencia:\n"))
            conta_corrente= conta_corrente-tranferencia
            print (" o saldo da conta corrente atualmente é: " + str(conta_corrente))

      case "2":
         op = int(input("escolha entre: \n1- poupança \n2- conta corrente \n"))
         if(op == 1):
            deposito = float(input("informe o valor da deposito:\n"))
            poupanca= poupanca+deposito
            print (" o saldo da poupança atualmente é: " + str(poupanca))
            
         if(op == 2):
            deposito = float(input("informe o valor da deposito:\n"))
            conta_corrente= conta_corrente+deposito
            print (" o saldo da conta corrente atualmente é: " + str(conta_corrente))

      case "3":
          op = int(input("escolha entre: \n1- poupança \n2- conta corrente \n"))
          if(op == 1):
            tranferencia = float(input("informe o valor da tranferencia:\n"))
            poupanca= poupanca-tranferencia
            print (" o saldo da poupança atualmente é: " + str(poupanca))
            
          if(op == 2):
            tranferencia = float(input("informe o valor da tranferencia:\n"))
            conta_corrente= conta_corrente-tranferencia
            print (" o saldo da conta corrente atualmente é: " + str(conta_corrente))


      case "4":
        op = int(input("escolha entre: \n1- poupança \n2- conta corrente \n"))
        if(op==1) :
         print (" a conta corrente atualmente é: " + str(conta_corrente))
        if(op==2):
           print (" a poupança atualmente é: " + str(poupanca))
          

          
 
  else:
    print("acessonegadodododdodododododoodod-")
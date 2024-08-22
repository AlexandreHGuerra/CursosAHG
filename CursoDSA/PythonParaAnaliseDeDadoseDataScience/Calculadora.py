while True:
    print("calculadora python")
    print("1 - soma")
    print("2 - subtracao")
    print("3 - multiplicacao")
    print("4 - divisao")    
    print("--------")    
    print("Informe a operacão")    
    print("--------")    
    x = ""
    x = input()
    if not x.isnumeric() :
        print ("somente numeros")   
        continue
    if int(x) < 0 or int(x) > 4 :
        print ("opaco incorreta. informe 1-4")
        continue
    
    # soma
    if x == "1" :

        op1 = "informe o primeiro valor"
        op2 = "informe o segundo valor"

    #subtracao        
    if x == "2" :

        op1 = "informe o primeiro valor"
        op2 = "informe o segundo valor"

    #multiplicacao    
    if x == "3" :

        op1 = "informe o primeiro valor"
        op2 = "informe o segundo valor"

    #divisao    
    if x == "4" :

        op1 = "informe o primeiro valor"
        op2 = "informe o segundo valor"
   


    print(op1)
    inpu1 = int(input())
    print(op2)
    inpu2 = int(input())


    if x == "1":
        print(inpu1 + inpu2)
    if x == "2":
        print(inpu1 - inpu2)
    if x == "3": 
        print(inpu1 * inpu2)
    if x == "4":
        print(inpu1 / inpu2)




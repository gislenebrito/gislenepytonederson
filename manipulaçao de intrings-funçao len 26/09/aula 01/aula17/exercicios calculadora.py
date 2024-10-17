
while True:
    num = int(input("1-adiçao\n2-subtraçao\n3-multiplicaçao\n4-divisao\n0-sair\n"))
    if num==0:
        print("saindo")
        break
    elif num==1:
        a= float(input("digite o valor a: "))
        b= float(input("digite o valor de b: "))
        total= a+b
        print("a soma dos dois numeros é: ",total)
    elif num==2:
        a= float(input("digite o valor a: "))
        b= float(input("digite o valor b: "))
        total= a-b
        print("a soma dos dois numeros é: ",total)
    
    elif num==3:
        a= float(input("digite o valor a: "))
        b= float(input("digite o valor b: "))
        total= a*b
        print("a soma dos dois numeros é: ",total)
    elif num==4:
        a= float(input("digite o valor a: "))
        b= float(input("digite o valor b: "))
        total= a/b
        print("a soma de dois numeros é: ",total)
        

while True:
    while True:
        nome = input("digite o seu nome: ")
        nomes = len(nome)
        if nomes < 3:
            print("tamanho invalido")
        else:
            print(nome)
            break

    while True:    
        idade = int(input("digite sia idade "))
        if idade >0 and idade <150:
            print(idade)
            break
        else:
            print("idade invalida")

    while True:
        sexo = input("digite seu sexo 'm' ,'f' ,'o' : ")
        if sexo != "m" or sexo != "f" or sexo != "o":
            print("sexo")
            break
        


    # salario= input("digite seu salario ")
    # sexo = input("digite seu sexo 'm' ,'f' ,ou 'o' ")
    # estado = input("digite seu estado 's', 'c', 'v' ,'d' ")
   


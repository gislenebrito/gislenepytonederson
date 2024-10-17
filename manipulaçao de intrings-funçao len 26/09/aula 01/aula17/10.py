#while,continue,
#em python
#while-exercicios(algoritimo que conta quantas vezes se pode reduzir em valor do numero passado como parametroate chegar a zero.ex:numero 100)

num= int(input("digite um valor"))
cont=0
while num >= 0:
    cont = cont+1 #quantas vezes entrou no loop
    num=num-1
    print(cont)
    
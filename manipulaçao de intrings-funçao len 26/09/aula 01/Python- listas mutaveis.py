#string ´imutavel ou seja nao consigo mudalas
#listas #mutaveis ja podem ser mudadas

frutas= ["banana","maça","cereja",]
frutas[0] = "pera"
frutas[-1]= "laranja"
print(frutas)

#fatiamento

uma_lista = ['a','b','c','d','e','f']
uma_lista[1:3] = ['x','y']
print(uma_lista)

#remover o elemento da lista
uma_lista=['a','b','c','d','e','f']
print(uma_lista)
print(len(uma_lista))

uma_lista[1:3]=[]
print(uma_lista)
print(len(uma_lista))

#inserir elementos dentro da listas
uma_lista = ['a','d','f']
uma_lista =(uma_lista)
uma_lista[1:1]=['b','c']
print(uma_lista)
uma_lista[4:4]=['e']
print(uma_lista)

#remover tambem , o ultimo nao entra
a=['um','dois','tres']
del a[1]
print(a)

#operador ponto(.)
#append = adiciona elemento no final da lista

a= [81,82,83]
a.append(5)
print(a)


#sort ordena a lista por ondem crescente
a= [81,82,83]
a.sort()
print(a)

#reverse=true= ordena ao contrario os numeros na lista



#index=posiçao que eu quero add o elemento
a=[1,2,3,4,5,6,7,8,9]
print(a.index(4))

#insert=
a=[88,81,82,83]
a.insert(1,100)#posiçao insira 100
print(a)

#a.pop = apaga o ultimo elemento da lista
a=[88,81,83,84,85,86]
a.pop()
print(a)

a.pop(0)
print(a)
#extend= unifica uma lista dentro de outra lista
listas=[1,2]
listas.extend[3,4]
print(listas)






#listas
x= "Ederson"
y=["ederson" , 18,20,34]

lista1 = [10,20,30,40]
lista2 = ["spam" , "bungee", "swallow" ]
print (lista1, lista2)

lista1 = ["oi" , 2.0,5, [10,20]]
print (lista1)
#len
lista1 = ["oi", 2.0, 5, [10,20]]
print (len(lista1))

numeros = [17, 123, 87, 34, 66, 8398, 44]
print(numeros[2])
print(numeros[9-8])
print(numeros[-2])
print(numeros[-1])
#quando tiver 2 elementos dentro da lista ou seja 2 colchetes imprime o primeiro e conta o outo dentro do mesmo elemento

frutas = ["maça","laranja","banana","cereja"]
print("maça" in frutas)
print("pera" in frutas)

frutas = ["maça","laranja","banana","cereja"]
print([1,2] + [3,4])
print(frutas + [6,7,8,9])

print([]*4)
print([1,2,["ola", "adeus"]]*2)

a = [1,2,3,4,5,6,7,8,9]
print (a)
print(max(a))
print(min(a))
print(sum(a))

#fatias de listas
uma_lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(uma_lista[1:3])
print(uma_lista[:4])
print(uma_lista[3:])
print(uma_lista[:])
print(uma_lista[0:6])

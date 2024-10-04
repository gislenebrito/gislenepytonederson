a="gislene"
print(len(a))
print(a.capitalize())
#o comando len serve para contar os elementos
#capitalize serve para mudar a primeira letra em maisculo

print(a.upper())
#comando upper serve para alterar todo o texto  em maiusculo
print(a.casefold())
#comando casefold para alterar todo o texto para o minusculo
print("gislene".upper())
print(a.lower())
#lower faz mesma funçao casefold
print(a.islower())
#esta perguntando se esta tudo minusculo la dentro;caso nao esteja vai imprimir true e se nao for vai imprimir falso
print(a.isupper())  
#identifica se todo o texto esta em maiusculo  
a="12345"
print(a.isdigit())
True
#como identificar se uma string so possui numeros inteiros
a="Gislene Brito"
print(a.replace("Brito","Costa"))
#esse substitui um elemento original por outro
a= "Ederson-Roberto-Costa"
print(a.split("-"))
#esse comando separa uma string usando virgula como separador
a="Ederson Roberto Costa"
print(a.find("Costa"))
x=16
#esse comando mostra onde esta a palavra costa na posiçao do indiçe
a= "ederson roberto costa"
print("costa"in a)
#esse comando in esta perguntando se tem a palavra costa dentro da variavel A
a="ederson costa"
print(a.count("o"))
#essa funçao conta quantidade de letra ou palavra 
s= "Ola,mundo!"
print(s[0])
print(s[2])
print(s[6])

s="Ola,mundo!"
print(s[-11])
print(s[-9])
print(s[-5])

s="Ola,mundo!"
print(s[1:3])
#esse pega uma fatia daquilo que quero








frutas=["pera", "uva", "banana", "manga","limao"]
frutas[1] = "laranja"
print (frutas)


janeiro=[10,20]
fevereiro=[30,40]
março=[50,60]
abril=[70,80]
maio=[90,95]
junho=[91,92]
julho=[15,16]
agosto=[17,18]
setembro=[19,20]
outubro=[21,22]
novembro=[23,24]
dezembro=[25,26]
temp=[]
temp.extend(janeiro)
temp.extend(fevereiro)
temp.extend(março)
temp.extend(abril)
temp.extend(maio)
temp.extend(junho)
temp.extend(julho)
temp.extend(agosto)
temp.extend(setembro)
temp.extend(outubro)
temp.extend(novembro)
temp.extend(dezembro)
print(temp)
print(sum(temp)/len(temp))
print(max(temp))
print(min(temp))

temp.sort()

print(temp)

temp.sort(reverse=True)





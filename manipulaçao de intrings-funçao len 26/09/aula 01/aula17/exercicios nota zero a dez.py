#faça um programa que peça uma nota,entre zero e dez.mostre uma mensagem caso o valor seja invalido e continue pedindo ate que o usuario informe um valor valido.

while True:
    valor =int(input("digite um valor de zero a dez"))
    if valor > 0 and valor < 10:
        print("valor valido!")
    else:
        print("valor invalido")

    
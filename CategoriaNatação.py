from time import sleep

ano = int(input("Digite seu ano de nascimento: "))
print("-=-" * 20)
print("Descobrindo qual categoria voce esta....")
sleep(2)
print("-=-" * 20)
if ano <=9:
    print("Categoria Mirim")
elif ano > 9 and ano <= 14:
    print("Categoria Infantil")
elif ano > 14 and ano < 19:
    print("Categoria Junior")
elif ano >= 19 and ano <= 20:
    print("Categoria Sênio")
else:
    print("Categoria Master")
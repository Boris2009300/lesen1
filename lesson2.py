import random
c = 0
simvol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parol = ''
a = int(input("Введите длину пароля: "))
if a >= 0 :
    print("Пароль генерируется")
    for i in range(a):
        parol += random.choice(simvol)
else:
    print("Длина пароля не может быть отрицательной или равной 0")
print("Ваш новый пароль-", parol)








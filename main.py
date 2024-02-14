from random import choice


simvols = '+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password = ''
len_pass = int(input('какой длины вы хотите сгенирировать пароль?'))
if len_pass <= 8:
    len_pass = 8
    print('Минимальное кол-во символов в пароле 8')
for i in range(len_pass):
    password += choice(simvols)
print(password)    




#this is an random password generator 
print('=====Password===Generator==========')
import random
char='ABCDEFGHIJKLMOPQRSTUVWXYZ1234567890@#&abcdefghijklmnopqratuvwxyz'
length=int(input('Enter length:'))
password=''
for a in range(length):
    password=password+random.choice(char)
#password+=random(char)
print(password)
if len(password) >= 8 :
    print("its a strong pass")
else :
    print("not so strong")
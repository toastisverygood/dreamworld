'''
    author:leon judd
    date: 31/07/2025
    
'''
import random
age = int(input('waht is your age: '))
print('Dreamworld - are you eligible to to take the rides ')
height = int(input('what is your height? cm:'))
if (height > 150 ):
    print(' you can go on the stratissphere,famly carts and scorpian carts')
if (height > 120  ):
    print('you can go on the fear,fall,invader,corkscrew roller coaster and bumber boats')
if (height > 89 and age > 5):
    print('you van go on the los banditos')
    if (age > 8):
        print('you can go on the robot roit')
if (height > 80):
    print('you can go on the log fume,gold rush,famly karts and the dogems')
if (height > 80 and age < 2 and age > 9 ):
    print('you can go in the fortes of fun')
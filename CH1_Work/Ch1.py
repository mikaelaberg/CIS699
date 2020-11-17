#Mikaela Berg 
#CIS699 Advanced Python 
#Fall20

#import statments:
import random


#R1.1
# def is_multiple(n,m):
#     return (int((m/n)))

# #for testing: 
# m = 16
# n = 4

# print(n, 'Goes into', m, is_multiple(n,m), 'times.')

def is_multiple(n,m):
    if (n % m):
        print('n is a multiple of m')
    else: 
        print('n is not a multiple of m')

#for testing: 
m = int(input('Pick a number(m):'))
n = int(input('Pick another'))

print(is_multiple(n,m))



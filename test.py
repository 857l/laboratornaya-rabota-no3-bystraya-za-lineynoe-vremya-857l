import random

f = open('input.txt', 'w')

for i in range(10**4):
    f.write(str(random.randint(0, 10**9)) + ' ')


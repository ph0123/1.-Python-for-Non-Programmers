#1 picking random numbers
import random
x = random.randint(1,10)
print(x)

print(random.random()) #will return float value

x = random.randint(1,3)
if x == 1:
    print("Yes")
elif x == 2:
    print("No")
else:
    print("Maybe")

#2.  choosing what fortune to show

x = random.randint(1,100)
print(f'Your lucky number for today is {x}')
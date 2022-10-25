#Functions and #parameters, return #comments
def add(a,b):
    return a+b

def add_and_sub(a,b):
    return a+b, a-b

a = 3 
b = 5
print(add(a,b))
print(add_and_sub(a,b))

#inputs

a = input("please enter a number: ")
b = input("please enter a number: ")
print(add_and_sub(a,b))
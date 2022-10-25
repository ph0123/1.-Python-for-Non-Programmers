
#Game loop
guess = input("select a number from 1 to 10: ")
print(guess)
correct_number = 5

while int(guess)!= correct_number:
    print("sorry!! wrong....")
    temp = correct_number<int(guess)
    if temp:
        print("correct number is lower than you guess value")
    else:
        print("correct number is higher than you guess value")
    guess = input("select a number from 1 to 10: ")

print("Congrats! the lucky number is ", guess)




#higher, lower and polish 
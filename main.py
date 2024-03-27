from random import randint
number=randint(1,100)
chances=5
while chances > 0:
    userResponse=int(input("GUESS THE NUMBER: "))



    if userResponse==number:


        print("YOU WON!")
        break
    elif userResponse > number:

        print("GUESSED NUMBER IS GREATER THAN NUMBER")
        chances-=1
    else:

        print("GUESSED NUMBER IS SMALLER THAN NUMBER")
        chances-=1
else:
    print("YOU LOST")
    print("the number is:",number)
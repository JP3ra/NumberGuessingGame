import random
print("Welcome to the number guessing game!")
print("\n")
print("---Rules of the Game---")
print("1. You have to guess a number between 1-10")
print("2. You get only 5 attempts")
print("\n")
print("Do you want to play this game?")
print("Yes/No")
ans = str(input())

if ans.lower()=="yes":
    num = random.randint(1,10)
    print("\n")
    print("Guess a number between 1-10:")
    num1 = int(input())
    attempts = 1

    while attempts!=5:
        if num1==num:
            print("\n")
            print("Your guess is correct!")
            print("You guessed the number in ", attempts, "attempts")

            break
        elif num1>num:
            print("Your guess was above the given number!")

            attempts+=1
        else:
            print("Your guess was below the given number!")

            attempts+=1
        print("Try Again")
        num1 = int(input())
    if attempts>=5:
        print("Sorry! You have exceeded the maximum number of attempts!")
    
else:
    print("Alright!")

            



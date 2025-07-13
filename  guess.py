import random
import time

number=random.randint(1, 10)

def intro():
    print("May I ask for your name")
    global name 
    name = input()
    print(name + ", we are going to play a game. I am thinking of a number between 1 and 10")

    if(number%2==0):
        x="even"
    else:
        x="odd"
    print("\nThis is an {} number".format(x))
    time.sleep(0.5)
    print("Guess")

def pick():
    guessesTaken = 0
    while guessesTaken < 6:
        time.sleep(.25)
        enter=input("Please Guess the number:,", name)
        try:
            guess = int(input())
            if guess<=10 and guess>=1:
                guessesTaken=guessesTaken+1
                if guessesTaken<6:
                    if guess<number:
                        print("The guess of the number that you have entered is too low")
                    if guess>number:
                        print("The guess of the number that you have entered is too high")
                    if guess != number:
                        time.sleep(0.5)
                        print("Try Again")
                    if guess==number:
                        break
                       
            
            if guess>10 or guess<1:

                print("That number isn't in the range!")
                time.sleep(.25)
                print("Please enter a number between 1 and 100")
        except:
            print("I don't think that "+enter+" is a number. Sorry")


if guess == number:
guessTaken = str(guessesTaken)
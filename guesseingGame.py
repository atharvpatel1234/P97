import random
number=random.randint(1,9)
chances=0



while(chances<5):
    GuessNumber=int(input("Guess a number between 1and9 :"))
    if number==GuessNumber:
        print("CONGRULATIONS YOU WON")
        break
    elif GuessNumber<number:
        print("YOUR GUESSES TOO LOW,GUESS A NUMBER HIGHER THAN",GuessNumber)    
    else:
        print("YOUR GUESSES TOO HIGH,GUESS A NUMBER LOWER THAN",GuessNumber)  
    chances=chances+1
if not chances <5:
    print("YOU LOSE,THE NUMBER IS ",number)








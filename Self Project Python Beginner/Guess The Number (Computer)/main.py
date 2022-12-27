import random

def guess(x): # function for Guess The Number (Computer)
    random_number = random.randint(1, x) # randit your focus
    guess = 0
    while guess != random_number: # while loop
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print("sorry, too low number. try again.")
        elif guess > random_number:
            print("sorry, too high number. try again.")
    
    print(f"Hore, You Great, Guess number is {random_number}, good job!")

# guess(25) # statement

def computer_guess(x): # function for Guess The Number (User)
    low = 1
    high = 25
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also be high b/c low = high
            feedback = input(f"Is {guess} too high (H), too low (L), or correctly!!")
        if feedback == 'h':
            high == guess - 1
        elif feedback == "l": 
            low = guess +1

    print(f'Great, The computer guessed your number {guess}, good job!')

computer_guess(10)
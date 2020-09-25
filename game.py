import random
def cointoss():
    call = str(input('Type "Heads" for heads or "Tails" for tails. Type "q" or "quit" to quit: ')) #Allows user to call side
    while call != 'q' and call != 'quit' and call != 'Q' and call != 'Quit': #Runs for however long user wants
        choices = ['Heads', 'Tails']
        result = random.choice(choices) #Picks random choice from given list
        if call == result and (call == 'Heads' or call == 'Tails'): #If result is the same as the call
                print('You chose: %s'%(call))
                print('The coin landed: %s'%(result))
                print('You win! \n')
        elif call != result and (call == 'Heads' or call == 'Tails'): #If result is not the same as the call
                print('You chose: %s'%(call))
                print('The coin landed: %s'%(result))
                print('You lose. \n')
        else:
            print('Error: Invalid input. Try again. \n') #For invalid inputs that are not q or quit
        call = str(input('Type "Heads" for heads or "Tails" for tails. Type "q" or "quit" to quit: ')) #Resets
    print('Thanks for playing! Goodbye.') #Prints when user asks to quit
cointoss()
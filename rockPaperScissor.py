### Rock paper scissors
### ask user to input
### computher will select


#### import random library
import random


# will return some value
def play():
    user = input("'r' for Rock, 's' for sessor, 'p' for paper : ") #ask user input
    print('You choose: '+ user)
    # will choose any value from this
    computer = random.choice(['r','p','s'])
    print('oponent choose: '+computer)

    if user == computer:
        return "tie"
    # r>s s>p p>r

    if is_win(user,computer):
        return 'you won'

    return 'You Lost!'





# for player winning conditions
def is_win(player, oponent):
    if (player == 'r' and oponent == 's')\
        or (player == 'p' and oponent == 'r')\
            or (player == 's' and oponent == 'p'):
        return True



print(play())







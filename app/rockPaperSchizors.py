import random

randNum   = random.randrange(0, 2)

print("Chose (0)rock (1)scissors (2)paper")
userOption = int(input())
option = []
option[0] = 'Rock'
option[1] = 'Paper'
option[2] = 'Scissors'

game = userOption + randNum;
print("Player plays "+option[userOption])
print("I play "+option[randNum])

if (game == 0) :
    print("Draw")
elif(game == 1) :
    print("Rock wins!")
elif(game == 2) :
    print("Paper wins")    
elif(game == 3) :
    print("Scissors wins")


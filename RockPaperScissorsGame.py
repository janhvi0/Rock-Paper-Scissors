#rock = 1  paper= 2  scissors = 3
#    1 2 3
# 1  d l w
# 2  w d l
# 3  l w d    conceptual matrix for the game

import random

def check(comp, user):
    if user == comp:
        return 0
    if user== 1 and comp == 2:
        return -1
    if user== 2 and comp == 3:
        return -1
    if user== 3 and comp == 1:
        return -1
    return 1

comp = random.randint(1,3)
user = int(input("Rock= 1\nPaper=2\nScissors=3\nmake your move:"))

print("You:",user)
print("Computer:",comp)

score = check(comp,user)
if score==0:
    print("Its a draw")
elif score==-1:
    print("You loose")
else:
    print("You Win")


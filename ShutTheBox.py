#python
import random

def roll():
    return random.randint(1,6);

def isSixOrUnder(state):
    total = 0
    for num in state:
        total = total + num
    return total <= 6

def checkShut(state):
   for num in state:
       if num != 0:
           return False
   return True

def makeRolls(state):
    rollTotal = 0
    rollOne = roll()
    if isSixOrUnder(state):
        rollTotal = rollOne
        print('Roll: {}'.format(rollTotal))
    else :
        rollTwo = roll()
        rollTotal = rollOne + rollTwo
        print('Roll: {}, {} -> {}'.format(rollOne,rollTwo,rollTotal))
    return rollTotal

def getScoreString(state):
    string = ''
    for num in state:
        if num != 0:
            string += str(num)
    return string

state = []
state = [i +1 for i in range(9)]

active = True
print(getScoreString(state))
rollTotal = makeRolls(state)
while active:
    invalidInput = False
    flip = input('Enter numbers to put down.\n').strip()
    tempState = state
    totalIn = 0
    if flip == 'end':
        print('Game over.  Your score: {}'.format(getScoreString(state)))
        exit()
    for char in flip:
        try:
            num = int(char)
            if(tempState[num-1] != 0 & num == 0):
                tempState[num-1] = 0
                totalIn = totalIn + num
            else :
                print('Unavalable number entered.  Try again.')
                invalidInput = True
                break
        except ValueError:
            print('Non-number entered.  Try again.')
            invalidInput = True
            break
    if not invalidInput:
        if(totalIn != rollTotal):
            print('Roll total {} and input total {} does not match. Try again.'.format(rollTotal,totalIn))
        else:
            state = tempState
            active = not checkShut(state)
            if(active):
                print('\n')
                print(getScoreString(state))
                rollTotal = makeRolls(state)
print('You shut the box!')
exit()
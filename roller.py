import random
die = (1,2,3,4,5,6)
result = []
doubles = [0]

def cast(dice):
    result.clear()
    for x in range(dice):
        result.append(random.choice(die))
    return result[x]

def dueDil():
        print("Is this place owned? or Do you want it?")
        input()
        print("Does anyone else?")
        input()
        if doubles[0] == 3:
            print("Your turn's over now, pass the dice.\n")

def turn():    
    doubles[0] = 0
    while doubles[0] < 3:
        cast(2)
        if doubles[0] == 2 and result[0] == result[1]:
            doubles[0] = 3
            print(str(result[0]) + " and " + str(result[1]) + " GO TO JAIL\n")
            input()
        elif result[0] == result[1]:
            doubles[0] += 1
            print("You got doubles, "+ str(doubles[0]) + \
                  " times.  "  + str(result[0]) + " and " + str(result[1]) + \
                  " means move " + str(result[0]+result[1])+ " spaces.")            
            dueDil()
        elif result[0] != result[1]:
            doubles[0] = 3
            print (str(result[0]) + " and " + str(result[1]) + \
                   " means move " + str(result[0]+result[1])+ " spaces.")            
            dueDil()
        input()

#turn()

x=0
while x < 100:
    turn()
    x+=1

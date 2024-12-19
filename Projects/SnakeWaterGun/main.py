import random
n = int(input('Enter The Round You Want To Play: '))
for i in range(1,n):
    userintput = input('Enter Your Choice: ')
    ChoiceDict = {
    'g' : -1,
    's' : 0,
    'w' : 1
    }
    Computer = random.choice([-1,0,1])
    Reversed_Dict = {
    -1 : "Gun",
    0 : "Snake",
    1 : "Water" 
    }
    you = ChoiceDict[userintput]
    print(f"You Chose {Reversed_Dict[you]}\nComputer Chose {Reversed_Dict[Computer]}")

    if(Computer == you):
        print('It`s an draw')
    else:
        if(Computer == 0 and you == 1):
            print('You Win!!')
        elif(Computer == 0 and you == -1):
            print('You Lose!!')
        elif(Computer == 1 and you == 0):
            print('You Win!!')
        elif(Computer == 1 and you == -1):
            print('You Lose!!')
        elif(Computer == -1 and you == 0):
            print('You Win!!')
        elif(Computer == -1 and you == 1):
            print('You Lose!!')
        else:
            print('Something Is Wrong')

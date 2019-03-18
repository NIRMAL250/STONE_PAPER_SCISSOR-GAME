import random
comp_score = 0
user_score = 0
n = 1
while(n<=3):
    print('        Your turn\n        ')
    option=input('Stone Paper Scissor: ')
    if(option.lower() != 'stone' and option.lower() != 'paper' and option.lower() != 'scissor'):
              print('\nEnter correct option')
              continue
    print()
    print("        Computer's turn\n        ")
    comp=random.randint(1,3)
    if(comp == 1):
        print('Computer chosen: stone\n')
        if(option.lower() == 'stone'):
            print('Tied')
        elif(option.lower() == 'scissor'):
             print('Computer scored\n')
             comp_score += 1
        else:
             print('You scored')
             user_score += 1

    if(comp==2):
        print('Computer chosen: paper\n')
        if(option.lower() == 'paper'):
            print('Tied')
        elif(option.lower() == 'stone'):
             print('Computer scored\n')
             comp_score += 1
        else:
             print('You scored')
             user_score += 1

    if(comp==3):
        print('Computer chosen: scissor\n')
        if(option.lower() == 'scissor'):
            print('Tied')
        elif(option.lower() == 'paper'):
             print('Computer scored\n')
             comp_score += 1
        else:
             print('You scored')
             user_score += 1
    
    n+=1
if(user_score>comp_score):
    print('        You won')
elif(user_score<comp_score):
    print('        Computer won')
else:
    print('        Tie match')
print('        TOTAL SCORE         \n')
print('%8s%13s'%('YOU','COMPUTER'))
print('%8d%13d'%(user_score,comp_score))

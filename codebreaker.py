import random
x=str(random.randint(100,999))
print("Welcome Code Breaker! Let us see if you can see my 3 digit number!")


while True:
    
    i=(input("What is your guess?"))

    if(x==i):
        print('Code Is broken!!!Congratulations..... ')
        break
        
    elif(i[0]==x[0] or i[1]==x[1] or i[2]==x[2]):
        print('MATCH')
        continue
        
    elif(i[0] in x or i[1] in x or i[2] in x):
        print('CLOSE')
        continue
        
    else:
        print('NOPE!!')
        continue
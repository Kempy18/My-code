import random
#player login
print("Player 1 login:")
Found = False
while Found == False:
    Player1_Name=str(input("Please enter your username:"))
    Player1_Password=str(input("Please enter your password:"))
    for line in open("User.txt","r").readlines():
        login=line.split()
        if Player1_Name == login[0] and Player1_Password == login[1]:
            Found = True
            break
        else:
            Found = False
        if Found == False:
            print("User not Valid. Re-enter Login for User 1")
            
print("Player 1 validated.")
print("Player 2 login:")
Found = False
while Found == False:
    Player2_Name=str(input("Please enter your username:"))
    Player2_Password=str(input("Please enter your password: "))
    for line in open("User.txt","r").readlines():
        login=line.split()
        if Player2_Name == login[0] and Player2_Password == login[1]:
            Found = True
            break
        else:
            Found=False
    if Found==False:
            print("User not Valid. Re-enter Login for User 2")
        
print("Player 2 validated.")
#player1 roll
player1point=0
start= input("Enter 'Roll' to start your turn:")
start== 'Roll'
print("Player 1 Roll the Dice:")
num1=random.randint(1,6)
print("You rolled a" , num1)
num2=random.randint(1,6)
print("You rolled a" , num2)
player1point=player1point+(num1+num2)
if num1==6 and num2==6:
    player1point=0
elif num1==num2:
    input("You rolled a double, enter 'Roll' to roll again:")
    start== 'Roll'
    num3=random.randint(1,6)
    print("You rolled a" , num3)
    player1point=player1point+num3
if player1point==0:
    player1point=0
elif ((num1+num2) %2 ==0):
     player1point=player1point+10
else:
    player1point=player1point-5
if player1point<0:
    player1point=0


print("Player1 score is", player1point)
#player2 roll
player2point=0
start= input("Enter 'Roll' to start your turn:")
start== 'Roll'
print("Player 2 Roll the Dice:")
num4=random.randint(1,6)
print("You rolled a" , num4)
num5=random.randint(1,6)
print("You rolled a" , num5)
player2point=player2point+(num4+num5)
if num4==6 and num5==6:
    player1point=0
elif num4==num5:
    input("You rolled a double, enter 'Roll' to roll again:")
    start== 'Roll'
    num6=random.randint(1,6)
    print("You rolled a" , num6)
    player2point=player2point+num6
if player2point==0:
    player2point=0
elif ((num4+num5) %2 ==0):
     player2point=player2point+10
else:
    player2point=player2point-5
if player2point<0:
    player2point=0
    
print("Player2 score is", player2point)
#winner statement
if player1point==player2point:
    print("Draw")
elif player1point>player2point:
    print("Player 1 wins with", player1point)
    print("Player 2 had", player2point)
else:
    print("Player 2 wins with",player2point)
    print("Player 1 had", player1point)

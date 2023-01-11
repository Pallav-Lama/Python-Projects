import random
print("Welcome to the Rock, Paper or Scissor game")
# Computer part
rand = random.randint(1,3)
if rand == 1:
    com = "R" 
elif rand == 2:
    com = "P" 
elif rand == 3:
    com = "S" 

# User part
user = input("Type 'R' to choose Rock, 'P' for Paper or 'S' for Scissor: ")

#Game Part
def compare(com, user):
    if com == user:
        return None
    elif user == "R":
        if com == "S":
            return True
        else:
            return False
    elif user == "P":
        if com == "R":
            return True
        else:
            return False
    elif user == "S":
        if com == "P":
            return True
        else:
            return False
    else:
        print("Please choose either capital R, P, S")
#game result part
result = compare(com, user)
print(f"You choose {user} and computer chooses {com}")
if result == True:
    print("Congrats!!! you won the game.")
elif result == False:
    print("Sorry! You loose. Please try again.")  
elif result == None:
    print("It seems a draw!")
    

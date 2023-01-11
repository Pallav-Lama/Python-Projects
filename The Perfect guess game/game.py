import random

r = random.randint(0,101)

p = int(input("Please guess a number between 0 and 100: "))
count = 1

while p > 0 or p <100:
    while p != r:
        if p<r:
            print("Guess higher number please")
            p = int(input("Please guess a number between 0 and 100: "))
            count += 1
        else:
            print("Guess lower number please")
            p = int(input("Please guess a number between 0 and 100: "))
            count += 1

    else:
        print("You won")
        print(f"You have guessed {count} times.")
        break

with open("highscore.txt") as f:
        highscore = int(f.read())

if count <= highscore:
    print(f'''Congrats you set the new highcore.
    The current highscore is {count}''')
    with open("highscore.txt", "w") as f:
        f.write(str(count))
    
else:
    print(f'''Wanna beat the current highscore? 
    You need to guess within {highscore} tries.''')

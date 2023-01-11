import random
try:
    try:
        a = int(input("Please Enter smaller bound: "))
        b = int(input("Please Enter greater bound: "))
    except:
        print("Please make sure you've given numeral value")

    rnum = random.randint(a, b)
    # print(rnum)

    print("Player 1's Turn: \n")
    isTrue = True
    count1 = 1
    while isTrue:
        try: 
            g1num = int(input(f"Guess the number between {a} and {b}: ")) 
        except:
            print("Please make sure you've given numeral value")
        if g1num > rnum:
            print("Wrong!!! Please guess lower number")
            count1 += 1
        elif g1num < rnum: 
            print("Wrong!!! Please guess higher number")
            count1 += 1
        else:
            print(f"You guess the right number within {count1} trials. \n")
            isTrue = False

    print("Player 2's Turn: \n")

    count2 = 1
    while isTrue == False:
        try:
            g2num = int(input(f"Guess the number between {a} and {b}: ")) 
        except:
            print("Please make sure you've given numeral value")
        if g2num > rnum:
            print("Wrong!!! Please guess lower number")
            count2 += 1
        elif g2num < rnum: 
            print("Wrong!!! Please guess higher number")
            count2 += 1
        else:
            print(f"You guess the right number within {count2} trials. \n")
            isTrue = True

    if count1 > count2:
        print(f"Player 2 wins by guessing within {count2} trials")
    elif count2 > count1:
        print(f"Player 1 wins by guessing within {count1} trials")
    else: 
        print(f"It seems a tie. Both guess within {count1} trials")
except:
    print("Oops!!! Something went wrong.")
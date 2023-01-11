try:
    n = int(input("How many apples does Harry Potter have?: "))
    mx = int(input("What is the maximum number of students he has?: "))
    mn = int(input("What is the minimum number of students he has?: "))
    
    if mx != mn:
        for i in range (mn, mx + 1):
            if n % i == 0:
                print(f"{i} is a divisor of {n}")
            else:
                print(f"{i} is not a divisor of {n}")
    else:
        print(f"minimum number ({mn}) is equal to maximum number({mx}) so this is not a range as {mx}-{mn} = {mx-mn}")
        if n % mx == 0:
            print(f"{mx} is a divisor of {n}")
        else:
            print(f"{mx} is not a divisor of {n}")
except Exception as e:
    print("Sorry there is some kind of error.")
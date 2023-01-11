import random
num = 3
# num = int(input("How many friends are there?: "))

# names = ["Pallav Lama", "Aaryan Tamang"]
# for i in range(num):
#     names.append(input("Enter your friends' names: "))

names = ["Pallav Lama", "Aaryan Tamang", "Palish Gurung"]
for name in names:
    n1 = random.randint(0, num-1)
    n2 = random.randint(0, num-1)
    splitFNames = names[n1].split(" ")
    splitSNames = names[n2].split(" ")
    print(f"{splitFNames[0]} {splitSNames[1]}")
    


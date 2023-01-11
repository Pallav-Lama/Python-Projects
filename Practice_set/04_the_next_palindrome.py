case = int(input("How many test cases do you wanna take?: "))

li = []
for i in range(case):
    li.append(int(input("Enter the number to find its next palindrome: ")))

for i in range (len(li)):
    b = li[i]
    istrue = True
    c= b
    while istrue:
        a = str(b)
        stli = [int(i) for i in a]
        # print(stli)

        stli2 = []
        for i in stli:
            stli2.append(i)

        stli2.reverse()

        if stli == stli2:
            print(f"Next palindrome for {c} is {b}")
            istrue = False
        else:
            b = b + 1












    





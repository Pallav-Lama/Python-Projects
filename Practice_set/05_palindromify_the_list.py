#This will determine the size of the list
try:
    sofl = int(input("Enter the size of the list: "))
except:
    print("The input is not a number")
    exit()

li = []
#The will make a list by appending the given input in the list (li)
for i in range(sofl):
    try:
        li.append(int(input("Enter the element of the list: ")))
    except:
        print("The input is not a number")
        exit()
# li = [1, 293, 3, 545]

li2 =[]
#if the element of the list is smaller than 10 then it will append the new list with the same element of the original list
for i in li:
    b = i
    d = b
    if b < 10:
        li2.append(b)
    else:
        #This will start the loop till all the element of the list is palindromized 
        isTrue = True
        while isTrue:
            li3 = []
            cli = [] 
            c = str(b)
            for i in c:
                cli.append(i)
            for i in range (len(c)):
                li3.append(c[i])
            li3.reverse()
            #if all the elements of the original list is palindromized then it will break the loop and append the palindromized element in new list
            if cli == li3:
                li2.append(b)
                isTrue = False
            else:
                b += 1

print(f"The list of next palindrome of {li} is: {li2}")

       


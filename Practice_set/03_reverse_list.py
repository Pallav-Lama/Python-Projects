sofl = int(input("Enter the size of list: "))
li = []
for i in range(sofl):
    x = input("Enter the list element: ")
    li.append(x)
print(li)

li.reverse()
print(li)

li = li[:: -1]
print(li)

li2=[]
count = 1
for i in li:
    i = li[len(li)-count]
    count += 1
    li2.append(i)

print(li2)
def multiFunc(number):
    table = [number * i for i in range(1,11)]
    table[4] = table[4] + 3 
    return table

def isCorrect(table, number):
    isThereError = False
    table2 = [number * i for i in range(1,11)]
    for i in range(len(table)):
        if table[i] != table2[i]:
            return i + 1

        

number = int(input("number: "))
table = (multiFunc(number))
print(table)

error = isCorrect(table, number)
print(f"There is an error in line number {error}.")


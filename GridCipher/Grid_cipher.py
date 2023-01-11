def str_to_cipher(userin):
    count=0
    a = {}
    b=[]
    c=''
    for alph in range(65, 91):
        for num in range(1, 6):
            if not 65 + count == 91:
                alnum = chr(alph) + str(num)
                a.update({chr(65 + count):alnum})
                count+=1
            else:
                break
    for letter in userin:
        letter = letter.upper()
        if letter == " ":
            b.append("/")
        else:
            b.append(f"{a[letter]}")

    for i in b:
        c+=i
    return c

userin=input("Please enter the word you want to cipher: ")
print(str_to_cipher(userin))
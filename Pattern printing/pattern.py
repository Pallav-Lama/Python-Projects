st ="enter your first sentence here"
st=st+" "
rev = ""
temp=""
# temp=""
# rev = " enter"
for word in st:
    if word != " ":
        temp = temp + word
    else:
        rev = rev + " " + temp
        temp=""
print(rev)
# Coding Challenge 2
# Name:
# Student No:

# A Morse code encoder/decoder

from genericpath import isfile
from posixpath import split


MORSE_CODE = (
    ("-...", "B"), (".-", "A"), ("-.-.", "C"), ("-..", "D"), (".", "E"), ("..-.", "F"), ("--.", "G"),
    ("....", "H"), ("..", "I"), (".---", "J"), ("-.-", "K"), (".-..", "L"), ("--", "M"), ("-.", "N"),
    ("---", "O"), (".--.", "P"), ("--.-", "Q"), (".-.", "R"), ("...", "S"), ("-", "T"), ("..-", "U"),
    ("...-", "V"), (".--", "W"), ("-..-", "X"), ("-.--", "Y"), ("--..", "Z"), (".-.-.-", "."),
    ("-----", "0"), (".----", "1"), ("..---", "2"), ("...--", "3"), ("....-", "4"), (".....", "5"), 
    ("-....", "6"), ("--...", "7"), ("---..", "8"), ("----.", "9"), ("-.--.", "("), ("-.--.-", ")"),
    (".-...", "&"), ("---...", ":"), ("-.-.-.", ";"), ("-...-", "="), (".-.-.", "+"), ("-....-", "-"),
    ("..--.-", "_"), (".-..-.", '"'), ("...-..-", "$"), (".--.-.", "@"), ("..--..", "?"), ("-.-.--", "!"),
    ("   ", " ")
)

def print_intro():
    print('''Welcome to Wolmorse
This program encodes and decodes Morse code.''')


def get_input():
    user_in = input("Would you like to encode (e) or decode (d): ").upper()
    while user_in == "E" or user_in == "D":
        file_or_con = input("Would you like to read from a file (f) or the console (c)?").upper()
        while file_or_con == "F" or file_or_con == "C":
            if file_or_con == "F":
                file_name = input("Enter Filename: ")
                while(not check_file_exists(file_name)):
                    print("Invalid filename")
                    file_name = input("Enter Filename: ")
                else:
                    process_lines(file_name, user_in)
                    sec_in = input("Would you like to encode/decode another message? (y/n): ").upper()
                    if(sec_in == "Y"):
                        get_input()
                    else:
                        return

                
            else:
                if user_in == "E":
                    message = input("What message would you like to encode: ").upper()                    
                    print(encode(message))
                    sec_in = input("Would you like to encode/decode another message? (y/n): ").upper()
                    if(sec_in == "Y"):
                        get_input()
                    else:
                        return
                else:
                    message = input("What message would you like to decode: ")
                    print(decode(message))
                    sec_in = input("Would you like to encode/decode another message? (y/n): ").upper()
                    if(sec_in == "Y"):
                        get_input()
                    else:
                        return
    else:
        get_input()


def encode(message):  
    enc_mess = []
    for element in range(0, len(message)):      
        for morse in MORSE_CODE:
            if message[element] in morse[1]:
                enc_mess.append(morse[0])
    result = " ".join(enc_mess)
    return result
            

def decode(message):
    res = []
    enc_mess = message.split("   ") 
    for word in enc_mess:
        for letter in word.split():
            for morse in MORSE_CODE:
                if letter == morse[0]: 
                    res.append(morse[1])
        res.append(" ")            
    result = " ".join(res)   
    return result

# ---------- Challenge Functions (Optional) ----------


def process_lines(filename, mode):
    with open(filename, 'r') as f:
        line = f.readline().upper()
        if(mode == "E"):
            write_lines(encode(line))
        else:
            write_lines(decode(line))


def write_lines(lines):
    with open("result.txt", 'w') as f:
        f.write(lines)



def check_file_exists(filename):
    return(isfile(filename))
    

def main():
    print_intro()
    get_input()
    
# Program execution begins here
if __name__ == '__main__':
    main()

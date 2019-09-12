from caesar import caesar

#Runs caesar cipher on input string using all 26
def allcaesar():
    msg = input("Enter string:  ")
    print("Input String:", msg)
    for i in range(1, 26):
        print("Shifted by", i, end=": ")
        caesar(msg, i)


allcaesar()

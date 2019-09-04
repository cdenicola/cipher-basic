from caesar import caesar


def allcaesar():
    msg = input("Enter string:  ")
    print("Input String:", msg)
    for i in range(1, 26):
        caesar(msg, i)


allcaesar()

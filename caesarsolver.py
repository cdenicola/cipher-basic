from caesar import caesar


# Runs all possible caesar cipher shifts on input string,
# outputting all results for user. Makes it easy
def all_caesar():
    msg = input("Enter string:  ")
    print("Input String:", msg)
    for i in range(1, 26):
        caesar(msg, i)


all_caesar()

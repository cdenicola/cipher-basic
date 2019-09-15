# File containing code for XOR ciphers
import secrets

# Basis for this cipher is contained in this proof
# x ^ 0 = x   --> x ^ 0 ^ 0 = x
# x ^ 1 = ~x  --> x ^ 1 ^ 1 = x


def xor_operation(message, key) -> int:
    return message ^ key


def xor_cipher():
    message = int(input("Input a number between 0 and 256: "))
    print("Generating random key...")
    key = secrets.randbits(8)
    cipher_message = xor_operation(message, key)
    print("Your encrypted message:", cipher_message, end="\n\n")
    user_response = ''
    while user_response not in ['y', 'n']:
        temp = input("Would you like to see your number deciphered? (y/n): ")
        user_response = temp[0].lower()
    if user_response == 'y':
        print("Your deciphered input:", xor_operation(cipher_message, key))

xor_cipher()
# This file contains methods to modify inputs into the format accepted functions in this program


# Converts numerical input to text return output where each number relates to a letter in the message according to an
# alphanumeric basis [0:A, 1:B, ..., 25:Z] {note: numbers this outside range will be removed}
# Input should have spaces between numbers in the same word and word_separator dignifies key used to separate words
# start_at_1 as true makes alphanumeric conversion along 1:A, 2:B, ..., 26:Z
def num_to_str(input_string, word_separator, start_at_1=False) -> str:

    character_array = input_string.replace(".", " .").replace(",", " ,").replace("!", " !").replace("?", " ?").replace(word_separator, " + ").split()
    return_string = ""

    for char in character_array:
        if char == '+':
            return_string += ' '
        elif char == '.' or char == '!' or char == '?':
            return_string += char
        else:
            input_integer = int(char)
            if start_at_1: # If True, uses 1:A, 2:B, ... , 26:Z format, else uses 0:A, 1:B, ... , 25:Z
                input_integer -= 1
            # If in range, convert to letter, else remove
            if 0 <= input_integer <= 25:
                nch = chr(input_integer + 65)
                return_string += nch
    return return_string

print(num_to_str("""4	18	15?	 	13	19	11!	 	19	3
22	25	13	11	4 15 14	 	19	24	 	22	11	24	17	22	15	9
6	11.	""", "	 	"))
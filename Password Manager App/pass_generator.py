import random

def create_pass():
    # Let's initialize all the characters for the password that we can use...

    letter_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
    'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    number_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    symbol_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters = random.randint(8, 10)
    symbols = random.randint(2, 4)
    numbers = random.randint(2, 4)

    characters = letters + symbols + numbers

    password = []

    while characters != 0:

        letter_index = random.randint(0, len(letter_list)-1)
        symbol_index = random.randint(0, len(symbol_list)-1)
        number_index = random.randint(0, len(number_list)-1)

        rand_index = random.randint(1, 3)

        condition = 1

        while condition == 1:

            if rand_index == 1 and letters != 0:
                password.append(letter_list[letter_index])
                letters -= 1
                break
            elif rand_index == 2 and symbols != 0:
                password.append(symbol_list[symbol_index])
                symbols -= 1
                break
            elif rand_index == 3 and numbers != 0:
                password.append(number_list[number_index])
                numbers -= 1
                break
            else:
                rand_index = random.randint(1, 3)
        
        characters -= 1
    new_pass = ''.join(password)

    return new_pass
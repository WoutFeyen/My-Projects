from random import randint

def generate_password(length):
    password = ""
    character_dump = "0123456789 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.-_&|é@\"#'()§èç{\}$[]µ£%ù<>"
    for _ in range(length):
        character_index = randint(1, len(character_dump)-1)
        password += character_dump[character_index ]
    return password

def validate_password(password):
    uppercase = False
    lowercase = False
    number = False
    space = False
    special_character = False

    for character in password:
        if "A" <= character <= "Z":
            uppercase = True
        elif "a" <= character <= "z":
            lowercase = True
        elif "0" <= character <= "9":
            number = True
        elif character == " ":
            space = True
        else:
            special_character = True
    
    score = 0
    if uppercase:
        score += 1
    if lowercase:
        score += 1
    if space:
        score += 1
    if number:
        score += 1
    if special_character:
        score += 1
    score += (len(password) // 5)

    if score < 6:
        print("Bad password")
    elif score < 11:
        print("Good password")
    elif score < 16:
        print("Great password")
    else:
        print("Epic password")


def make_choice():
    chosen_function = input("Type in the number of the function you want to use: ")
    if chosen_function not in "12":
        print("invalid option")
        return make_choice()
    return chosen_function


print("This code has 2 functions: \n 1) generating a password \n 2) validating a password")
chosen_function = make_choice()

if chosen_function == "1":
    length = int(input("Give the desired lenth of the password: "))
    print(generate_password(length))
else:
    validate_password(input("Type in the password you want to validate: "))
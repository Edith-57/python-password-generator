import random

lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
special = "!~@#$%^&*()_+"

no_special_set = lower_case + upper_case + numbers
all_characters = no_special_set + special

def generatePassword(length):
    if length < 12:
        length = 12

    password = [
        random.choice(lower_case),
        random.choice(upper_case),
        random.choice(numbers)
    ]

    if spl.lower() == "yes":
        password.append(random.choice(special))

    char_pool = all_characters if spl.lower() == "yes" else no_special_set

    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return "".join(password)

length = int(input("Enter the password length: "))
spl = input("Include special characters? (yes/no): ")

satisfied = "no"
while satisfied.lower() == "no":
    print(generatePassword(length))
    satisfied = input("Satisfied with this password? (yes/no): ")
else:
    print("Thanks for using the password generator!")
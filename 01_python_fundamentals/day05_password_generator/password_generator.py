import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# For letters
rand_letter=""
for i in range(nr_letters):
    random_letter=random.choice(letters)
    rand_letter+=random_letter

# For symbols
rand_symbol=""
for i in range(nr_symbols):
    random_symbol=random.choice(symbols)
    rand_symbol+=random_symbol

# For numbers
rand_num=""
for i in range(nr_numbers):
    random_number=random.choice(numbers)
    rand_num+=random_number

password=rand_letter+rand_symbol+rand_num
print(f"Password (easy version): {password}")

# Hard version
adv_pass_list=list(password) # converting easy version password into a list
random.shuffle(adv_pass_list) # shuffling the list
adv_pass_string="".join(adv_pass_list) # converting list back to string
print(f"Password (Advanced version): {adv_pass_string}")
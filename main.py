alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя"
encrypt = input("Enter your message: ")
key = int(input("Please enter a key (number 1-26): "))
encrypt = encrypt.lower()
encrypted = ""

for letter in encrypt:
    position = alphabet.find(letter)
    new_position = position + key
    if letter in alphabet:
        encrypted += alphabet[new_position]
    else:
        encrypted += letter

print(encrypted)
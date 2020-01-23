import copy
alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
reversed_alphabet = copy.copy(alphabet)
reversed_alphabet.reverse()
def myFunction(text):
    text = list(text)
    for i in range(len(text)):
        for j in range(len(alphabet)):
            if text[i] == alphabet[j]:
                text[i] = reversed_alphabet[j]
                break
    temp = "".join(text)
    print(temp)
myFunction('Автандил'.lower())
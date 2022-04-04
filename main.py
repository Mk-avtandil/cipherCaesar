from string import ascii_lowercase as eng_alphabet


class CipherCaesar:
    def __init__(self, text, key):
        if key > 26:
            raise Exception('Значение ключа больше 26')
        self.__text = text.lower()
        self.__key = key
        self.__alphabet = eng_alphabet * 2

    def encript(self):
        encrypted = ""
        for letter in self.__text:
            position = self.__alphabet.find(letter) + self.__key
            if letter in self.__alphabet:
                encrypted += self.__alphabet[position]
            else:
                encrypted += letter
        return encrypted

    def decrypt(self):
        self.__text = self.encript()
        decrypted = ""
        for letter in self.__text:
            position = self.__alphabet.find(letter) - self.__key
            if letter in self.__alphabet:
                decrypted += self.__alphabet[position]
            else:
                decrypted += letter
        return decrypted

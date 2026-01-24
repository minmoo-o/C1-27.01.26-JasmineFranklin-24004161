def caesar_cipher(sentence, shift):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""

    for char in sentence:
        if char in alphabet:
            index = alphabet.index(char)
            index = index + shift

            if index >= 26:
                index = index - 26

            result = result + alphabet[index]
        else:
            result = result + char

    return result


sentence = input("Enter a sentence: ")
shift = int(input("Enter shift: "))

print(caesar_cipher(sentence, shift))


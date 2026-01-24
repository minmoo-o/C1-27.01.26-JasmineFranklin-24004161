text = input("Enter text: ")

alphabet = "abcdefghijklmnopqrstuvwxyz"

for letter in alphabet:
    count = 0
    i = 0
    while i < len(text):
        if text[i] == letter:
            count += 1
        i += 1
    if count > 0:
        print(letter + ":", count)

dictionary_file = open("./dictionary.txt")
dictionary = dictionary_file.read()
dictionary_file.close()
dictionary_list = dictionary.split("\n")

original_file = open(",/excerpt.txt")
original = original_file.read()
original_file.close()

original_list = original.split()
for word in original_list:
    word = word.replace(".","")
    word = word.replace(",","")
    print(word)
    if word in dictionary_list:
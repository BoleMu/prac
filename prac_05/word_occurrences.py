str = input("Text: ")
word = {}
keys = str.split()
for key in keys:
    if key in word.keys():
        word[key] = word[key] + 1
    else:
        word[key] = 1
print(word)
alpha = "abcdefghijklmnopqrstuvwxyz"

with open("unfiltered.txt") as file:
    filtered = []
    words = file.readlines()
    for word in words:
        dont_add = False
        word = word.strip().lower()
        for letter in word:
            if letter not in alpha:
                dont_add = True
        if not dont_add:
            filtered.append(word)

with open("words.txt", "w") as file:
    for word in filtered:
        file.write(word + "\n")
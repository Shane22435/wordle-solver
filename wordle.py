print("How many letters are in the word?")
num_letters = int(input())

with open("words.txt") as file:
    words = file.readlines()
    #add all words of num_letters length to a list
    words = [word.strip() for word in words if len(word.strip()) == num_letters]
    
#create a frequency dictionary for each letter in each position in words
freqpos_dict = {}
for word in words:
    for i in range(num_letters):
        if word[i] not in freqpos_dict:
            freqpos_dict[word[i]] = 1
        else:
            freqpos_dict[word[i]] += 1
    #my thinking of this is that we can assign higher values to words that contain higher frequency letters
    
    
#create a dictionary of words and their corresponding values, removing value to duplicate letters
word_values = {}
for word in words:
    value = 0
    seen = []
    for letter in word:
        if letter not in seen:
            value += freqpos_dict[letter]
            seen.append(letter)
    word_values[word] = value
    
#create an ordered list of words based on their values
ordered_words = sorted(word_values, key=word_values.get, reverse=True)

print("The best word is: ", ordered_words[0])
    


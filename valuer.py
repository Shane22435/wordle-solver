def Value(prev_guess="", prev_feedback=[]):
    #import the words from the valid-wordle-words.txt file
    with open("valid-wordle-words.txt") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
        
    #create a frequency dictionary for each letter in each position in words
    freqpos_dict = {}
    for word in words:
        for i in range(1,5):
            if word[i] not in freqpos_dict:
                freqpos_dict[word[i]] = 1
            else:
                freqpos_dict[word[i]] += 1
                    
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
        
    if prev_guess:
        #create a dictionary of words that are still possible
        possible_words = {}
        for word in word_values:
            possible = True
            for i in range(1,5):
                if prev_feedback[i-1] == 1 and prev_guess[i] != word[i]:
                    possible = False
                    break
                elif prev_feedback[i-1] == 2 and prev_guess[i] not in word:
                    possible = False
                    break
            if possible:
                possible_words[word] = word_values[word]
        word_values = possible_words    
    
    
    #create an ordered list of words based on their values
    ordered_words = sorted(word_values, key=word_values.get, reverse=True)
    print(f'your next guess should be {ordered_words[0]}')

    return ordered_words
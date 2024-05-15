import random
        
def Value(prev_guess="", prev_feedback=[], words = []):            
    if prev_guess:
        #create a new list of words
        new_words = []
        for word in words:
            valid = True
            for i in range(len(prev_guess)):
                if prev_feedback[i] == 1:
                    if word[i] != prev_guess[i]:
                        valid = False
                        break
                elif prev_feedback[i] == 2:
                    if word[i] == prev_guess[i]:
                        valid = False
                        break
                elif prev_feedback[i] == 0:
                    if prev_guess[i] in word:
                        valid = False
                        break
            if valid:
                new_words.append(word)
        words = new_words
        #print(f'Number of words left: {len(words)}')
        
        freqpos_dict = {}
        for word in words:
            for i in range(len(prev_guess)):
                if word[i] not in freqpos_dict:
                    freqpos_dict[word[i]] = 1
                else:
                    freqpos_dict[word[i]] += 1
                    
        word_values = {}
        for word in words:
            value = 0
            seen = []
            for letter in word:
                if letter not in seen:
                    value += freqpos_dict[letter]
                    seen.append(letter)
            word_values[word] = value
            
    words = sorted(words, key = lambda x: word_values[x], reverse = True)
    #print(f"your next guess should be: {words[0]}")
    return words

YELLOW = '\033[33m'
BRIGHT_GREEN = '\033[92m'
RESET = '\033[0m'

def wordle():
    with open("newwords.txt") as file:
        words = file.readlines()
        words = [word.strip() for word in words]
    guesses = 0
    word = random.choice(words)
    guess = ""
    while True:
        feedback = []
        if not guess:
            guess = random.choice(words)
        else:
            guess = words[0]
            
        if guess == word:
            #print(f"{BRIGHT_GREEN}{word}{RESET}")
            #print(f"{BRIGHT_GREEN}You win!{RESET}")
            break
        else:
            guesses += 1
            if guesses == 6:
                #print(f"Out of guesses! The word was {YELLOW}{word}{RESET}")
                break
            else:
                for letters in range(len(word)):
                    if guess[letters] == word[letters]:
                        #print(f"{BRIGHT_GREEN}{guess[letters]}{RESET}", end="")
                        feedback.append(1) # correct letter in correct position
                    elif guess[letters] in word:
                        #print(f"{YELLOW}{guess[letters]}{RESET}", end="")
                        feedback.append(2) # correct letter in wrong position
                    else:
                        #print(guess[letters], end="")
                        feedback.append(0) # incorrect letter
                #print()
        words = Value(guess, feedback, words)
    return guesses

total_guesses = 0
for i in range(2500):                
    total_guesses += wordle()

print(f"Average guesses: {total_guesses/1000}")
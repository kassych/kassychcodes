# Prompt the user to enter a word
# and assign it to the user_word variable.
word_without_vowels = ""
user_word = input("Please enter a Word to process: ")
user_word = user_word.upper()
for letter in user_word:
    if letter  != 'A': 
        if letter != 'E':
            if letter != 'I':
                if letter != 'O':
                    if letter != 'U':
                        word_without_vowels += letter

print (word_without_vowels)

    


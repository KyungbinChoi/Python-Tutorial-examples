def occuringVowels(word):
    Vowel = ('A', 'E', 'I', 'O', 'U')
    upper_word = word.upper()
    occur_vowels = []
    for i in Vowel:
        if i in upper_word:
            occur_vowels.append(i)

    result = sorted(occur_vowels)
    return result

word = input("Enter a word: ")
print("The following vowels occur in the word: {}".format(occuringVowels(word)))
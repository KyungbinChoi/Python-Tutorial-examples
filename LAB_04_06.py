def isVowelWord(word):
    # confirm whether contain all vowels
    Vowel = ('A', 'E', 'I', 'O', 'U')
    upper_word = word.upper()
    for i in Vowel:
        if i not in upper_word: return False
        else: return True

word = input("Enter a word: ")

if isVowelWord(word):
    print(word, "contains every vowels")
else:
    print(word, "doesn't contains every vowels")



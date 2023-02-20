
#ES UN ANAGRAMA

def is_anagram(word_one, word_two):
    if word_one.lower() == word_two.lower():
        return False
    return word_one == word_two

print(is_anagram("Amor", "Roma"))

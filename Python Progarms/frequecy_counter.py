def word_frequency(string_words):
    #hello hello words
    string_words = "".join(char.lower() for char in string_words if char.isalnum() or char.isspace())
    count = {}
    for words in string_words.split():
        count[words] = count.get(words, 0) +1
    
    return count


print(word_frequency("Hello! world hello"))
print("!".isalnum())
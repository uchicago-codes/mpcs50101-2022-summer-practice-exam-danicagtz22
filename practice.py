def count_vowels(word):
    counter = 0
    vowels = ["a","e","i", "o", "u"]
    for l in word:
        if l in vowels:
            counter += 1
    return counter
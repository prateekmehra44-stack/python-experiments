sentence = input("Enter sentence: ")
words = sentence.split()

unique_words = set(words)

print("Unique words count:", len(unique_words))
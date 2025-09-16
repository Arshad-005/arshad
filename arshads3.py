def analyse_sentence(sentence):
    words = sentence.lower().split()
    total_words = len(words)
    unique_words = len(set(word))
    most_common = Counter(words).most_common(1)[0]

    return total_words, unique_words, most_common
sentence = "python is great and python is fun and useful"
total, unique, common = analyse_sentence(sentence)

print("Total words:", total)
print("Unique words:", unique)
print("Most frequent word:", common[0], "appears", common[1], "times")

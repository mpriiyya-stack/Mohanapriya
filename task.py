text = """
I am learning Python.
learning Python in intern.
Python is easy to learn.
Python is user-friendly.
"""
words = text.lower().replace(".", "").split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
print("Word Frequency:\n")
for word, count in sorted_words:
    print(word, ":", count)
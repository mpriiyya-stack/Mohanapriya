word_count = {}
try:
    with open("input.txt", "r") as f:
        text = f.read().lower()
    words = text.split()
    for word in words:
        word = word.strip(".,!?")
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print("Word Frequency:\n")
    for word, count in word_count.items():
        print(word, ":", count)
except FileNotFoundError:
    print("Sorry! input.txt was not found.")


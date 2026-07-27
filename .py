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

    # Print the results
    print("Word Frequency:\n")

    for word, count in word_count.items():
        print(word, ":", count)

    # Write the results to a new file
    with open("word_counts.txt", "w") as f:
        for word, count in word_count.items():
            f.write(f"{word}: {count}\n")

    print("\nWord counts saved to 'word_counts.txt' successfully!")

except FileNotFoundError:
    print("Sorry! input.txt was not found.")


word_count = {}

try:
    with open("input.txt", "r") as f:
        text = f.read().lower()

    # Check if the file is empty
    if text.strip() == "":
        print("The input file is empty. Please add some text.")
    else:
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

        with open("word_counts.txt", "w") as f:
            for word, count in word_count.items():
                f.write(f"{word}: {count}\n")

        print("\nWord counts saved to 'word_counts.txt' successfully!")

except FileNotFoundError:
    print("Sorry! input.txt was not found.")
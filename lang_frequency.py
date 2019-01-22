import re
from collections import Counter
import sys


def load_data(filepath):
    with open(filepath) as filepointer:
        return filepointer.read()


def get_most_frequent_words(text, number_of_printed_words=5):
    words = re.findall(r"\w+", text.lower())
    words_counter = Counter(words)
    return words_counter.most_common(number_of_printed_words)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit("Please pass file name as a param")

    filename = sys.argv[1]
    try:
        file_content = load_data(filename)
    except FileNotFoundError:
        sys.exit("Please use correct file name")

    most_frequest_words = get_most_frequent_words(
        file_content, number_of_printed_words=10)
    number_of_words = len(most_frequest_words)
    print("Top {} most frequent words from file {}:".format(
        number_of_words,
        filename
    ))
    print("\n".join(x[0] for x in most_frequest_words))

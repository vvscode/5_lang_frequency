import re
from collections import Counter
import sys

number_of_printed_words = 10


def load_data(filepath):
    with open(filepath) as filepointer:
        return filepointer.read()


def get_most_frequent_words(text):
    words = re.findall(r"\w+", text.lower())
    words_counter = Counter(words)
    return words_counter.most_common(number_of_printed_words)


if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        file_content = load_data(filename)
        most_frequest_words = get_most_frequent_words(file_content)
        number_of_words = len(most_frequest_words)
        print("Top {} most frequent words from file {}:".format(
            number_of_words,
            filename
        ))
        print("\n".join(x[0] for x in most_frequest_words))
    except IndexError:
        print("Please pass file name as a param")
    except FileNotFoundError:
        print("Please use correct file name")

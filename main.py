import string


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print_report(file_contents)


def count_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count


def print_report(book):
    print("--Begin report of I don't want to hard code this ---")

    print(f"{count_words(book)} words found in the document")

    dict_result = char_count(book)
    alphabet = list(string.ascii_lowercase)
    for i in alphabet:
        print(f"The '{i}' character was found {dict_result[i]} times")

    print("--- End report ---spaces")


def char_count(book):
    booc = book.lower()
    words = booc.split()
    result_dict = {}
    spaces = 0

    for char in booc:
        if char == " ":
            spaces += 1

    result_dict[" "] = spaces

    for word in words:
        for char in word:
            if char in result_dict:
                result_dict[char] += 1
            else:
                result_dict[char] = 1

    return result_dict


main()

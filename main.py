def sort_on(dict):
    return dict["num"]

def count_characters(file_contents):
    result = dict()
    for letter in file_contents:
        if letter.isalpha():
            if letter.lower() in result:
                result[letter.lower()] += 1
            else:
                result[letter.lower()] = 1
    
    char_count = []
    for item in result:
        char_count.append({"name": item, "num": result[item]})

    char_count.sort(reverse=True, key=sort_on)
    #print(char_count)
    for i in range(len(char_count)):
        print(f"The '{char_count[i]['name']}' character was found {char_count[i]['num']} times")

def count_words(file_contents):
    print(f"{len(file_contents.split())} words found in the document")


def print_text(file_contents):
    print(file_contents)


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print("--- Begin report of books/frankenstein.txt ---")    
    count_words(file_contents)
    print("")
    count_characters(file_contents)
    print("--- End report ---")

main()
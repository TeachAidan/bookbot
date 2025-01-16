def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = num_of_words(text)
    chars_dict = count_chars(text)
    sorted_list = dict_to_list(chars_dict)

    print(f"Number of words in the book: {num_words}")
    print("Number of each character in the book:")

    for item in sorted_list:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
        

def num_of_words(text):
    words = text.split()
    return len(words)

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_chars(text):
    characters = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def dict_to_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
    

    
    

main()

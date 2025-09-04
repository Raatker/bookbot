def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

main()
import sys

def main():
    from stats import get_book_text
    from stats import get_num_words
    from stats import check_freq

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    print("============ BOOKBOT ============")

    BookText = get_book_text(filepath)
    print("Analyzing book found at " + filepath + "...")

    print("----------- Word Count ----------")

    WordCount = get_num_words(BookText)
    print("Found " + WordCount + " total words")

    print("--------- Character Count -------")
    
    check_freq(BookText.lower())

    print("============= END ===============")
    
main()
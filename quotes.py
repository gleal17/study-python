def read_file():
    quotes = open("./quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()

read_file()
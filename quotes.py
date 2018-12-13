import urllib

def read_file():
    quotes = open("./quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_check)
    output = connection.read()
    connection.close()
    print ("\n-> Profanity: " + output)

read_file()
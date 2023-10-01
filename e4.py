import webbrowser

user_term = input("Enter a search term: ").replace(" ","+")

webbrowser.open("https://search.brave.com/search?q=" + user_term)
# open() expects a URL as a string in the argument.
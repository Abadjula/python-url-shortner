url_input = input("Enter a url to shorten: ")
if url_input.startswith("https://" or "http://"):
    pass
else:
    url_input = "https://" + url_input
user_input = input("Enter a word (this word will be you shortner name): ")
html = f"<a href=\"{url_input}\"><h1>{user_input}</h1></a>"
html_file = open("Shortner.html", "w")
html_file.write(html)
html_file.close()
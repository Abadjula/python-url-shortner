try:
    url_input = input("Enter a url to shorten: ")
    if url_input.startswith("https://" or "http://"):
        pass
    else:
        url_input = "https://" + url_input
    user_input = input("Enter a word (this word will be you shortner name): ")
    Size = int(input("Pick the size of your url\nOptions are 1-6. 1 is the largest and 6 is the smallest: "))
    if Size in range(1, 7):
        html = f"<a href=\"{url_input}\"><h{Size}>{user_input}</h{Size}></a>"
        html_file = open("Shortener.html", "w")
        html_file.write(html)
        html_file.close()
    else:
        print("Invalid option")
except ValueError:
    print("You have entered a string not a number")

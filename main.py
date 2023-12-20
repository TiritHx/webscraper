# from terminal import colors
from requests_html import HTMLSession
from config import isconfig, print_options
from scrape import get_site

# isconfig() # will use that later for saving users time

session = HTMLSession()
user_input = 0
print_options()
while input != "q":
    user_input = input("Please select option\n")
    match user_input:
        case "q":
            print("Closing application")
            break
        case "r":
            url = input("Enter the website URL\n")
            print(get_site(session, url))
        case _:
            print("Command not recognized")
session.close()
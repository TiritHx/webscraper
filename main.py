from requests_html import HTMLSession
from config import isconfig, print_options
from functions import read_site

# isconfig() # will use that later for saving users time

session = HTMLSession()
user_input = 0
print_options()
while input != "q":
    user_input = input("Please select option\n")
    match user_input:
        case "q" | "quit":
            print("Closing application")
            break
        case "h" | "help":
            print_options()
        case "r" | "read":
            read_site(session)
        case _:
            print("Command not recognized")
session.close()
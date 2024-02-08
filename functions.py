import re, os, requests
# import requests_html
from bs4 import BeautifulSoup


def get_site(session, url):
    try:
        res = session.get(url)
        res.html.render()
        print("Response status: " + str(res.status_code))
        return BeautifulSoup(res.html.html, "html.parser").prettify()
    except requests.ConnectionError:
        print("Site not rechable:", url)
        print("Check if website that you want to connect is operating")
        return 0

def File_Exist(file_name):
    if not os.path.isfile(file_name): 
        file = open(file_name, 'x', encoding="utf-16")
        file.close()
        print("Output file '" + file_name + "' created")
        return False
    print("Output file detected")
    return True 

def read_site(session):
    url = input("Enter the website URL\n")
    if re.search("^https://.", url):
        res = get_site(session, url)
        if res != 0:
            print(res)
            print("\nDo you want to store it into a file? Y/N")
            user_input = input("Please select option\n")
            if user_input in ["Y", "y", "YES", "Yes", "yes", "yea"]:
                file_name = input("Enter file name:\n")
                match input("Choose file extension to use\n"):
                    case "txt" | ".txt":
                        file_name += ".txt"
                        print("Used .txt extension")
                    case "html" | ".html":
                        file_name += ".html"
                        print("Used .html extension")
                    case "php" | ".php":
                        file_name += ".php"
                        print("Used .php extension")
                    case "xml" | ".xml":
                        file_name += ".xml"
                        print("Used .xml extension")
                    case "json" | ".json":
                        file_name += ".json"
                        print("Used .json extension")
                    case "htm" | ".htm":
                        file_name += ".htm"
                        print("Used .htm extension")
                    case "xhtml" | ".xhtml":
                        file_name += ".xhtml"
                        print("Used .xhtml extension")
                    case _:
                        file_name += ".txt"
                        print("Extension not recognized, used .txt instead")
                File_Exist(file_name)
                file = open(file_name, "wb")
                file.write(res.encode("utf-16"))
                file.close()
                print("Site saved succesfully")
            else:
                print("This site will not be stored")
    else:
        print("This url does not meet the requirements\nRequirements to meet: url needs to start with 'https://'")

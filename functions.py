import re
import requests_html
import requests
from bs4 import BeautifulSoup


def get_site(session, url):
    try:
        res = session.get(url)
        res.html.render()
        print("Response status: " + str(res.status_code))
        return BeautifulSoup(res.html.html, "html.parser").prettify()
    except requests.ConnectionError:
        print("Site not rechable", url)
        return 0

def read_site(session):
    url = input("Enter the website URL\n")
    if re.search("^https://.", url):
        res = get_site(session, url)
        if res != 0:
            print(res)
    else:
        print("This url does not meet the requirements\nRequirements to meet: url needs to start with 'https://'")
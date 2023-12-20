from bs4 import BeautifulSoup

def get_site(session, url):
    res = session.get(url)
    return BeautifulSoup(res.html.html, "html.parser").prettify()
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from tools.HTMLtools.HTMLanalyzer import *
from pprint import pprint
from tools.HTTPtools.HTTPconstructor import *
from tools.SQLtools.SQLscanner import *

session = HTMLSession()
res = session.get("https://www.wikipedia.org/")

doc = res.html.html
forms = get_forms(doc)
formdict = get_form_data(forms[0])
data = form_to_http(formdict)

pprint(data)






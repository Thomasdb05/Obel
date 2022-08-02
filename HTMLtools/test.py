from bs4 import BeautifulSoup
from requests_html import HTMLSession
from HTMLanalyzer import *
from pprint import pprint

session = HTMLSession()
res = session.get("https://www.youtube.com/channel/UC_qCr_KL0-dUWHwTNzVKziA/featured")
#res.html.render()
doc = res.html.html
forms = get_forms(doc)
pprint(get_form_data(forms[0]))






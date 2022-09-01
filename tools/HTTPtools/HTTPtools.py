from select import select
from unittest import result
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from pprint import pprint
from urllib.parse import urljoin
import webbrowser
import sys

from tools.HTMLtools.HTMLanalyzer import *

#Create dict with {name: value} structure for each input field in form
def form_to_http(form):
    data = {}

    for field in form['inputfields']:
        data[field['name']] = field['value']
    
    return data

def get_form_result(form):
    http_data = form_to_http(form)
    url = urljoin(url, form["action"])

    if form["method"] == "post":
        result = session.post(url, data=http_data)
    elif form["method"] == "get":
        result = session.get(url, params=http_data)
    
    return result
    
#def fill_base_values(form, Allsame, AllDintffere):
    

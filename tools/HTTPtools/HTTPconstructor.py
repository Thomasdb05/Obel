from select import select
from bs4 import BeautifulSoup

#Create dict with {name: value} structure for each input field in form
#Sets all values to default specified in form dict
def form_to_http(form):
    data = {}

    for field in form['inputfields']:
        data[field['name']] = field['value']
    
    return data

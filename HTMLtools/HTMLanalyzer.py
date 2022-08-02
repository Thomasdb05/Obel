from select import select
from bs4 import BeautifulSoup


def get_forms(doc):
    soup = BeautifulSoup(doc, 'html.parser')
    return soup.find_all('form')


def get_form_data(form):
    formdata = {}

    #get form action (url direct)
    action = form.attrs.get("action").lower()
    #POST/GET/DELETE etc, GET is default if unspecified in HTML
    method = form.attrs.get("method", "get").lower()
    formdata['action'] = action
    formdata['method'] = method

    #get text inputfields
    inputfields = []
    for inputfield in form.find_all('input'):
        name = inputfield.attrs.get('name')
        type = inputfield.attrs.get('type', 'text')
        defaultval = inputfield.attrs.get('value', "")

        inputfields.append({'type': type, 'name': name, 'value': defaultval})
    
    #get select fields
    for selectfield in form.find_all('select'):
        name = selectfield.attrs.get('name')
        options = []
        defaultval = ""

        for option in selectfield.find_all('option'):
            optionval = option.attrs.get('value')
            if not optionval == "":
                options.append(optionval)
                #if selected, set as default
                if option.attrs.get('selected'):
                    defaultval = optionval

        #if not default set and list not empty, just select first
        if defaultval == "" and len(options) > 0:
            defaultval = options[0]
        
        inputfields.append({'type': 'select', 'name': name, 'values': options, 'value': defaultval})

    #get textareas
    for textarea  in form.find_all('textarea'):
        name = textarea.attrs.get('name')
        value = textarea.attrs.get('value', "")
        inputfields.append({'type': 'textarea', 'name': name, 'value': value})

    formdata['inputfields'] = inputfields

    return formdata
from tools.HTTPtools.HTTPtools import get_form_result
from logger import *

def user_input_values(inputvalues):
    new_inputvalues = inputvalues.copy()
    for i in range(0, len(inputvalues)):
        if inputvalues['value'] == "":
            new_inputvalues[i] = input('What value would you like to use for "' + input['name'] + '"?')


#def random_input_values(inputvalues, seed):
    

def input_base_form_values(inputvalues, custom_values = False, random_values = False, random_seed = 0):
    if custom_values:
        return user_input_values(inputvalues)
    if random_values:
        return random_input_values(inputvalues, random_seed)


def is_bool_result_vuln(stdpage, truepage, falsepage):
    return truepage is stdpage and not falsepage == truepage

#takes inputfields part of form dictorionary
#returns two dictionaries containing all form input values, there is only one changed input in both dicts, the changed input depends on the fieldindex
def get_true_false_pair(inputfields, fieldindex, payloadindex, payloads):
    currentinput_true = inputfields[:]
    currentinput_false = inputfields[:]
    #get payloads corresponding to payloadindex in payloads, even always true while uneven always false
    true_payload = payloads[payloadindex]
    false_payload = payloads[payloadindex+1]

    currentinput_true[fieldindex]['value'] += true_payload
    currentinput_false[fieldindex]['value'] += false_payload

    return (currentinput_true, currentinput_false)


#Takes form data that isnot yet formatted to HTTP
def check_form_vuln_boolbased(form):
    global generic_bool_based_list

    #uses the form's default value, if unsuccesful, fill in values
    inputfields = form['inputfields']
    answer = ask("Form with empty default parameters found, would you like to use random values?", ["I would like to use Random values", "I want to Customize the values used"], ['R', 'C'], 'R')
    
    match answer:
        case 'R':
            inputfields = input_base_form_values(inputfields, random_values=True, random_seed=0)
        case 'C':
            inputfields = input_base_form_values(inputfields, custom_values=True)
    
    payloads = generic_bool_based_list

    for i in range(0, len(inputfields)):
        check_val_vuln_boolbased(form, i, payloads)



#Input with modified base values can be given here for inputfields
#Returns successful payload index, if none successful, return -1
def check_val_vuln_boolbased(form, fieldindex, payloads):
    inputfields = form['inputfields'] 

    result_default = get_form_result(form)
    for i in range(0, len(payloads), 2):
        #first is true and second is false
        pair = get_true_false_pair(inputfields, fieldindex, i, payloads)
        inputfields_true = pair[0]
        inputfields_false  = pair[1]

        #Create 2 forms with both of the payload modified input values
        true_form = form.copy()
        false_form = form.copy()
        true_form['inputfields'] = inputfields_true
        false_form['inputfields'] = inputfields_false

        result_true = get_form_result(true_form)
        result_false = get_form_result(false_form)
        
        if is_bool_result_vuln(result_default, result_true, result_false):
            return i

    return -1




    
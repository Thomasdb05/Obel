def file_to_list(dir, filename):
    with open('DATA/' + dir + '/' + filename) as f:
        lines = f.read().splitlines()
    return lines

def initiliaze():
    #Initialize payloads
    global generic_bool_based_list
    global generic_error_based_list
    global generic_time_based_list
    global generic_union_based_list
    global questions_list

    generic_bool_based_list = file_to_list('payloads', 'generic-bool-based.txt')
    generic_error_based_list = file_to_list('payloads', 'generic-error-based.txt')
    generic_time_based_list = file_to_list('payloads', 'generic-time-based.txt')
    generic_union_based_list = file_to_list('payloads', 'generic-union-based.txt')
    questions_list = file_to_list('logging', 'questions.txt')




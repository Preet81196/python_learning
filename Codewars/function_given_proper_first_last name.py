'''Your task is to create a function that, given a proper first and last name, will return the correct alias. '''
def alias_gen(f_name, l_name, FIRST_NAME=None, SURNAME=None):
    s1 = FIRST_NAME.get(f_name[0].upper(),'')
    s2 = SURNAME.get(l_name[0].upper(),'')
    if not s1 or not s2:
        return 'Your name must start with a letter from A - Z.'
    return s1 + ' ' + s2
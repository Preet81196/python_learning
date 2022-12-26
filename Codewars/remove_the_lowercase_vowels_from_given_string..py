'''Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.'''


def shortcut(s):
    return s.replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')


shortcut('hello')

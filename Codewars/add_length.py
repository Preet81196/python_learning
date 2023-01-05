def add_length(str_):

    return [word + ' ' + str(len(word)) for word in str_.split()]


print(add_length('apple ban')) 
print(add_length('you will win')) 
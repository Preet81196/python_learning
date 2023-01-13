'''Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.

Note: a and b are not ordered!'''

def get_sum(a,b):
    if a == b:
        return a
    elif a > b:
        return sum(range(b,a+1))
    else:
        return sum(range(a,b+1))

print(get_sum(0,9))
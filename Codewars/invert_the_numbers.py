'''how to invert the numbers'''

def invert(lst):
    return [-i for i in lst]

if __name__ == '__main__':
    print(invert([1,2,3,4,5]))
    print(invert([1,-2,3,-4,5]))
    print(invert([]))





#Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order.
#Essentially, rearrange the digits to create the highest possible number.

def Descending_Order(num):

    num = str(num)
    num = list(num)
    num.sort(reverse=True)
    num = ''.join(num)
    return int(num)

if __name__ == '__main__':
    print(Descending_Order(123456789))
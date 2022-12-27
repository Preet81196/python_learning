'''find the nearest square number, nearest_sq(n), of a positive integer n'''
def nearest_sq(n):
    return round(n ** 0.5) ** 2


if __name__ == '__main__':
    print(nearest_sq(10))
    print(nearest_sq(111))
    print(nearest_sq(9999))


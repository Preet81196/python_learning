def find_common_divisors(num1, num2):
    divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors.append(i)
    return divisors

def main():
    num1 = int(input())
    num2 = int(input())
    print(find_common_divisors(num1, num2))

if __name__ == '__main__':
    main()

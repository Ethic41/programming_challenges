# Author: Dahir Muhammad Dahir
# Date: 23rd-05-2019 08:28 PM


def main():
    divisors_list = []
    for i in range(1, 1000000):
        for j in range(1, i):
            if i % j == 0:
                divisors_list.append(j)
        if sum(divisors_list) == i:
            print((i, divisors_list))
        divisors_list = []


if __name__ == "__main__":
    main()

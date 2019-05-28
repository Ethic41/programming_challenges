# Author: Dahir Muhammad Dahir
# Date: 27th-05-2019 07:58 PM
# About: elephant and candies problem 4rm codechef, LECANDY


def main():
    test_case = int(input())

    for case in range(test_case):
        number_of_elephant, candies = map(int, input().split(' '))
        elephant_demand = sum(list(map(int, input().split(' '))))

        if elephant_demand > candies:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()

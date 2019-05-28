# Author: Dahir Muhammad Dahir
# Date: 27th-05-2019 09:07 PM
# About: chef and notebook problem from codechef


def main():
    test_cases = int(input())

    for case in range(test_cases):
        total_pages, available_pages, budget, n = map(int, input().split(' '))
        required_pages = total_pages - available_pages

        lucky = False
        for i in range(n):
            pages, cost = map(int, input().split(' '))

            if (pages >= required_pages) and (cost <= budget):
                lucky = True

        if lucky:
            print("LuckyChef")
        else:
            print("UnluckyChef")


if __name__ == '__main__':
    main()

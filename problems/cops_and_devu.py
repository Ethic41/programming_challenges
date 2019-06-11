# Author: Dahir Muhammad Dahir
# Date: 06-June-2019 11:47 PM
# About: I will tell you later
 
 
def main():
    test_cases = int(input())

    for case in range(test_cases):
        m, x, y = list(map(int, input().strip().split()))
        houses = list(map(int, input().strip().split()))

        max_searchable_house = x * y
        default_safe_houses = 100 - max_searchable_house

        for house in houses:
            if house > default_safe_houses:
                default_safe_houses -= 1

        print(default_safe_houses)


if __name__ == "__main__":
    main()

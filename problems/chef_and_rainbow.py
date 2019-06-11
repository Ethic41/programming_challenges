# Author: Dahir Muhammad Dahir
# Date: 01st-June-2019 06:16 AM
# About: i will tell you later


def main():
    test_cases = int(input())

    for case in range(test_cases):
        n = int(input())

        array = list(map(int, input().strip().split()))

        if n % 2 != 0:
            first_part = array[:int(n/2)]
            last_part = array[int(n/2)+1:]

            if array[int(n/2)] == 7 and set(first_part) == set(last_part) == {1, 2, 3, 4, 5, 6}:
                print("yes")
            else:
                print("no")
        else:
            first_part = array[:int(n/2)]
            last_part = array[int(n/2):]

            if set(first_part) == set(last_part) == {1, 2, 3, 4, 5, 6, 7}:
                print("yes")
            else:
                print("no")


if __name__ == "__main__":
    main()

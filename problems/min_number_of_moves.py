# Author: Dahir Muhammad Dahir
# Date: 1st-June-2019 02:02 AM
# About: i will tell you later


def main():
    test_cases = int(input())
    counter = 0
    step = 0

    for case in range(test_cases):
        n = int(input())

        salaries = list(map(int, input().strip().split()))

        while max(salaries) != min(salaries):
            max_salary_loc = salaries.index(max(salaries))
            difference = max(salaries) - min(salaries)
            for i in range(n):
                if i != max_salary_loc:
                    salaries[i] += difference
            counter += difference
            step += 1

        print(counter)
        counter = 0


if __name__ == "__main__":
    main()

# Author: Dahir Muhammad Dahir
# Date: 23rd-05-2019
# About: 3n + 1 problem


max_chain = 0


def main():
    # this hold the beginning and ending values as integers
    start, end = map(int, input().split())
    # looping through all integers from 'start' to 'end'
    for i in range(start, end+1):
        chain = algorithm(i)
        global max_chain  # since we are referencing the global variable 'max_chain'
        # testing if the current chain is greater than last known maximum chain
        if chain > max_chain:
            max_chain = chain
    print("{} {} {}".format(start, end, max_chain))


def algorithm(n):
    # this is the 3n+1 Algorithm implementation
    counter = 1  # counter is one because the n is part of the chain length
    if n == 1:
        return 1

    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        counter += 1

    return counter


if __name__ == "__main__":
    main()

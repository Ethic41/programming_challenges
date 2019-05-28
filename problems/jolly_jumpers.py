# Author: Dahir Muhammad Dahir
# Date: 26th-05-2019 01:22 PM


def main():
    jolly = False

    while True:
        line = input()
        if not line:
            break

        n, sequence = line.split(" ", 1)
        n = int(n)
        sequence = list(map(int, sequence.split(" ")))

        for i in range(n):
            if i == n - 1:
                if jolly:
                    print("Jolly")
                else:
                    print("Not jolly")
                break

            if 1 <= abs(sequence[i] - sequence[i+1]) <= n - 1:
                jolly = True
            else:
                print("Not jolly")
                break
        jolly = False


if __name__ == "__main__":
    main()

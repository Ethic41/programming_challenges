# Author: Dahir Muhammad Dahir
# Date: 23rd-05-2019 03:07 PM
# About: Minesweeper problem

# definitions: x is adjacent to y, if x is either before or after y, above or below y
# before or after the value above or below y and vice-versa
# note: that "0 0" will be used as the end of input


def main():
    input_mine_field = []  # this will hold input mine field for the current iteration
    output_mine_field = []  # this will hold output mine field for the current iteration

    mine_field_counter = 0

    while True:  # loop continuously since we don't know number of fields
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break

        for _ in range(n):
            input_mine_field.append(list(input()))

        num_of_line = n
        for field_line_index in range(num_of_line):
            if field_line_index == 0:
                line = get_output_line(input_mine_field[field_line_index], m, below=input_mine_field[field_line_index + 1])
                output_mine_field.append(line)
                continue

            if field_line_index == (num_of_line - 1):
                line = get_output_line(input_mine_field[field_line_index], m, above=input_mine_field[field_line_index - 1])
                output_mine_field.append(line)
                continue

            line = get_output_line(input_mine_field[field_line_index], m, below=input_mine_field[field_line_index + 1], above=input_mine_field[field_line_index - 1])
            output_mine_field.append(line)

        mine_field_counter += 1
        print("Field #{}:".format(mine_field_counter))
        for mine_field_line in output_mine_field:
            print(mine_field_line)

        input_mine_field = []
        output_mine_field = []


def get_output_line(line, m, above=None, below=None):
    current_output_line = ""
    num_of_items = m
    adjacent_mine_count = 0
    if above and below:
        for item_index in range(num_of_items):
            if item_index == 0:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    if below[item_index] == "*":
                        adjacent_mine_count += 1
                    if below[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    if above[item_index] == "*":
                        adjacent_mine_count += 1
                    if above[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue
                
            if item_index == num_of_items - 1:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    if below[item_index] == "*":
                        adjacent_mine_count += 1
                    if below[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    if above[item_index] == "*":
                        adjacent_mine_count += 1
                    if above[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue

            if line[item_index] == "*":
                current_output_line += "*"
            else:
                if line[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if line[item_index - 1] == "*":
                    adjacent_mine_count += 1
                if below[item_index] == "*":
                    adjacent_mine_count += 1
                if below[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if below[item_index - 1] == "*":
                    adjacent_mine_count += 1
                if above[item_index] == "*":
                    adjacent_mine_count += 1
                if above[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if above[item_index - 1] == "*":
                    adjacent_mine_count += 1
                current_output_line += str(adjacent_mine_count)
                adjacent_mine_count = 0
        return current_output_line

    if below:
        for item_index in range(num_of_items):
            if item_index == 0:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    if below[item_index] == "*":
                        adjacent_mine_count += 1
                    if below[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue

            if item_index == num_of_items - 1:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    if below[item_index] == "*":
                        adjacent_mine_count += 1
                    if below[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue

            if line[item_index] == "*":
                current_output_line += "*"
            else:
                if line[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if line[item_index - 1] == "*":
                    adjacent_mine_count += 1
                if below[item_index] == "*":
                    adjacent_mine_count += 1
                if below[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if below[item_index - 1] == "*":
                    adjacent_mine_count += 1
                current_output_line += str(adjacent_mine_count)
                adjacent_mine_count = 0
        return current_output_line

    if above:
        for item_index in range(num_of_items):
            if item_index == 0:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    if above[item_index] == "*":
                        adjacent_mine_count += 1
                    if above[item_index + 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue

            if item_index == num_of_items - 1:
                if line[item_index] == "*":
                    current_output_line += "*"
                else:
                    if line[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    if above[item_index] == "*":
                        adjacent_mine_count += 1
                    if above[item_index - 1] == "*":
                        adjacent_mine_count += 1
                    current_output_line += str(adjacent_mine_count)
                    adjacent_mine_count = 0
                continue

            if line[item_index] == "*":
                current_output_line += "*"
            else:
                if line[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if line[item_index - 1] == "*":
                    adjacent_mine_count += 1
                if above[item_index] == "*":
                    adjacent_mine_count += 1
                if above[item_index + 1] == "*":
                    adjacent_mine_count += 1
                if above[item_index - 1] == "*":
                    adjacent_mine_count += 1
                current_output_line += str(adjacent_mine_count)
                adjacent_mine_count = 0
        return current_output_line


if __name__ == "__main__":
    main()

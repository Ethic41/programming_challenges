# Author: Dahir Muhammad Dahir
# Date: 24th-05-2019 09:07 PM


def main():
    registers = {'0': '000', '1': '000', '2': '000', '3': '000', '4': '000', '5': '000', '6': '000', '7': '000', '8': '000', '9': '000'}
    ram = []
    eip = 0
    instruction_counter = 0

    end_of_current_ram = False
    test_cases = int(input())  # hold our test cases
    input()  # the first blank line

    for case in range(test_cases):
        for i in range(1000):
            if not end_of_current_ram:
                line = input()  # collecting ram input
                if not line:
                    end_of_current_ram = True
                else:
                    ram.append(line)
            else:
                ram.append('000')  # initializing the remaining RAM to 000s

        end_of_current_ram = False  # setting the flag back to default

        while True:
            opcode = ram[eip]

            if opcode.startswith("1"):
                instruction_counter += 1
                break

            if opcode.startswith("0"):
                if int(registers[opcode[2]]) == 0:
                    instruction_counter += 1
                    eip += 1
                    continue
                else:
                    instruction_counter += 1
                    eip = int(registers[opcode[1]])
                    continue

            if opcode.startswith("2"):
                registers[opcode[1]] = '{:0>3}'.format(opcode[2])
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('3'):
                registers[opcode[1]] = '{:0>3}'.format((int(registers[opcode[1]]) + int(opcode[2])) % 1000)
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('4'):
                registers[opcode[1]] = '{:0>3}'.format((int(registers[opcode[1]]) * int(opcode[2])) % 1000)
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('5'):
                registers[opcode[1]] = '{:0>3}'.format(registers[opcode[2]])
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('6'):
                registers[opcode[1]] = '{:0>3}'.format((int(registers[opcode[1]]) + int(registers[opcode[2]])) % 1000)
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('7'):
                registers[opcode[1]] = '{:0>3}'.format((int(registers[opcode[1]]) * int(registers[opcode[2]])) % 1000)
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('8'):
                registers[opcode[1]] = ram[registers[opcode[2]]]
                instruction_counter += 1
                eip += 1
                continue

            if opcode.startswith('9'):
                ram[registers[opcode[2]]] = registers[opcode[1]]
                instruction_counter += 1
                eip += 1
                continue

        print(instruction_counter)
        instruction_counter = 0
        ram = []
        eip = 0
        registers = {'0': '000', '1': '000', '2': '000', '3': '000', '4': '000', '5': '000', '6': '000', '7': '000', '8': '000', '9': '000'}


if __name__ == "__main__":
    main()

# Author: Dahir Muhammad Dahir
# Date: 23rd-05-2019 11:06 PM
# About: the_trip
# note: since we need to divide the expense
# evenly then we could just sum and then divide
# by the number of students


def main():
    while True:
        student_amount = []
        number_of_student = int(input())
        amount_exchanged = 0.00

        if number_of_student == 0:
            break

        for i in range(number_of_student):
            student_amount.append(float(input()))

        total_amount = float("%.2f" % sum(student_amount))
        target_amount = float("%.2f" % (total_amount / float(number_of_student)))

        for amount in student_amount:
            if amount > target_amount:
                amount_difference = float(amount - target_amount)
                amount_exchanged += amount_difference

        print("${}".format("%.2f" % amount_exchanged))


if __name__ == "__main__":
    main()

"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def sum_digits(nr):
    if type(nr) == "int":
        return -1
    nr = abs(nr)
    x = 0
    while nr:
        x += nr % 10
        nr = nr // 10
    return x


def main():

    int_number = 222222222222222222
    digit_sum = sum_digits(int_number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()

def reverse_number(number):
    num_list = []

    while int(number) > 0:
        num = number[::-1]
        for digit in num:
            num_list.append(digit)
        return num_list

print(reverse_number(input('enter a number')))


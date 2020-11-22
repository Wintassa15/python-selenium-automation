# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary
# representation of that number. You can guarantee that input is non-negative.
#
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
# test.assert_equals(count_bits(0), 0)
# test.assert_equals(count_bits(4), 1)
# test.assert_equals(count_bits(7), 3)
# test.assert_equals(count_bits(9), 2)
# test.assert_equals(count_bits(10), 2)

number = int(input('Enter a number: '))


def to_bin(n):
    bin_string = ''
    while n > 0:
        bin_string += str(n % 2)
        n = n // 2
    result = bin_string[::-1]
    return result.count("1")


print(to_bin(number))

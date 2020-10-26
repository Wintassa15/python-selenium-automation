# Create a function that will take a string as an input and return the 1st non-unique letter of a string.
# “Google” => “l”
# “Amazon” => “m”
# If there are no unique letters, return an empty string: “xoxoxo” => “”.
# How would you test it? How would you handle edge cases?
def non_unique_letter(unique_letter):

    for char in unique_letter:
        if char in unique_letter:
            return char
        else:
            return ""


print(non_unique_letter("Google"))

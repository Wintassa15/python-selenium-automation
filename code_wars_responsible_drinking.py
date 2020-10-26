# Examples
#
# "1 beer"  =>  "1 glass of water"
# "1 shot, 5 beers and 1 glass of wine"  =>  "7 glasses of water"
# Notes
#
# To keep the things simple, we'll consider that anything with a number in front of it is a drink: "1 bear" => "1 glass of water" or "1 chainsaw and 2 pools" => "3 glasses of water"
# The number in front of each drink lies in range [1; 9]


def hydrate(drink_string):
    character_number = 0
    for char in drink_string:
        if char.isnumeric():
            character_number += int(char)
    return str(character_number) + "glass of water"


print(hydrate("1 shot, 5 beers and 3 glass of wine"))

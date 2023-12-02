from aoc_tools import Advent_Timer
from re import compile as compile_regex

DIGIT_REGEX = compile_regex(r"(?:zero|one|two|three|four|five|six|seven|eight|nine|\d)")
DIGIT_MAP = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        data = file.read().splitlines()
    return data

def find_first_digit(string):
    for char in string:
        if char.isdigit():
            return char

def find_last_digit(string):
    return find_first_digit(reversed(string))

def get_calibration_value_1(string):
    digits = find_first_digit(string) + find_last_digit(string)
    return int(digits)

def digit_to_int(digit):
    if digit in DIGIT_MAP:
        return DIGIT_MAP[digit]
    else:
        return int(digit)

def get_calibration_value_2(string):
    all_digits = DIGIT_REGEX.findall(string)
    return 10*digit_to_int(all_digits[0]) + digit_to_int(all_digits[-1])

def sum_calibration_values(data, calibration_value_func):
    total = 0
    for string in data:
        total += calibration_value_func(string)
    return total

if __name__ == "__main__":
    timer = Advent_Timer()
    
    data = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_01 = sum_calibration_values(data, get_calibration_value_1)
    print(f"Star_01: {star_01}")
    timer.checkpoint_hit()
    
    star_02 = sum_calibration_values(data, get_calibration_value_2)
    print(f"Star_02: {star_02}")
    timer.checkpoint_hit()

    timer.end_hit()

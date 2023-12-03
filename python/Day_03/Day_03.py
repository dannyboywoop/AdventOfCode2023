from re import compile as compile_regex
from typing import NamedTuple
from aoc_tools import Advent_Timer

NUMBER_REGEX = compile_regex(r"\d+")
SYMBOL_REGEX = compile_regex(r"[^\.\d]")

class Position(NamedTuple):
    row: int = 0
    col: int = 0
    
    def __add__(self, other):
        assert isinstance(other, Position)
        return Position(self.row + other.row, self.col + other.col)
    
    def __sub__(self, other):
        assert isinstance(other, Position)
        return Position(self.row - other.row, self.col - other.col)

def read_data(input_file="input.txt"):
    numbers: dict[Position, str] = {}
    symbols: dict[Position, str] = {}
    with open(input_file, 'r') as file:
        for row, line in enumerate(file.read().splitlines()):
            numbers |= {Position(row, match.start()): match.group()
                                   for match in NUMBER_REGEX.finditer(line)}
            symbols |= {Position(row, match.start()): match.group()
                                   for match in SYMBOL_REGEX.finditer(line)}
    return numbers, symbols

def get_all_adjacent(start_pos:Position, length:int):
    adjacent: set[Position] = set()

    # end points
    adjacent.add(start_pos-Position(col=1))
    adjacent.add(start_pos+Position(col=length))

    # above and below
    for col_delta in range(-1, length+1):
        adjacent.add(start_pos+Position(row=-1, col=col_delta))
        adjacent.add(start_pos+Position(row=1, col=col_delta))
    
    return adjacent

def is_part_number(number: str, start_pos: Position, symbols:dict[Position, str]):
    adjacent_symbols = get_all_adjacent(start_pos, len(number)).intersection(symbols)
    return bool(adjacent_symbols)

def star_01(numbers, symbols):
    part_number_total = 0
    for pos, number in numbers.items():
        if is_part_number(number, pos, symbols):
            part_number_total += int(number)
    return part_number_total

if __name__ == "__main__":
    timer = Advent_Timer()
    
    numbers, symbols = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(numbers, symbols)}")
    timer.checkpoint_hit()
    
    star_02 = None
    print(f"Star_02: {star_02}")
    timer.checkpoint_hit()

    timer.end_hit()

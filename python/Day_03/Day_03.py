from re import compile as compile_regex
from typing import NamedTuple
from functools import cache
from math import prod
from aoc_tools import Advent_Timer

NUMBER_REGEX = compile_regex(r"\d+")
SYMBOL_REGEX = compile_regex(r"[^\.\d]")

class Position(NamedTuple):
    row: int = 0
    col: int = 0
    
    def __add__(self, other):
        assert isinstance(other, Position)
        return Position(self.row + other.row, self.col + other.col)
    

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
    adjacent.add(start_pos+Position(col=-1))
    adjacent.add(start_pos+Position(col=length))

    # above and below
    for col_delta in range(-1, length+1):
        adjacent.add(start_pos+Position(row=-1, col=col_delta))
        adjacent.add(start_pos+Position(row=1, col=col_delta))
    
    return adjacent

def get_adjacent_symbol_positions(number:str, start_pos: Position, symbols:dict[Position, str]):
    return get_all_adjacent(start_pos, len(number)).intersection(symbols)

def get_part_numbers_and_symbol_neighbours(numbers, symbols):
    part_numbers: list[int] = []
    symbol_neighbours: dict[Position, list[int]] = {position: [] for position in symbols}

    for pos, number in numbers.items():
        adjacent_symbol_positions = get_adjacent_symbol_positions(number, pos, symbols)
        number_int = int(number)
        if adjacent_symbol_positions:
            part_numbers.append(number_int)
        for adjacent_symbol_position in adjacent_symbol_positions:
            symbol_neighbours[adjacent_symbol_position].append(number_int)
    
    return part_numbers, symbol_neighbours

def star_01(part_numbers):
    return sum(part_numbers)

def star_02(numbers, symbols, symbol_neighbours):
    total = 0
    for position, symbol in symbols.items():
        if symbol == "*" and len(symbol_neighbours[position]) == 2:
            total += prod(symbol_neighbours[position])
    return total
        

if __name__ == "__main__":
    timer = Advent_Timer()
    
    numbers, symbols = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    part_numbers, symbol_neighbours = get_part_numbers_and_symbol_neighbours(numbers, symbols)
    print(f"Finished preprocessing data!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(part_numbers)}")
    timer.checkpoint_hit()
    
    print(f"Star_02: {star_02(numbers, symbols, symbol_neighbours)}")
    timer.checkpoint_hit()

    timer.end_hit()

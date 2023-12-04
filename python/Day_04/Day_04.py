from dataclasses import dataclass
from re import compile as compile_regex
from functools import cached_property
from aoc_tools import Advent_Timer


@dataclass
class Card:
    winning_nums: set[int]
    my_nums: set[int]

    @staticmethod
    def from_str(card_str:str):
        _, numbers_str = card_str.split(": ")
        winning_nums_str, my_nums_str = numbers_str.split(" | ")
        winning_nums = set(int(num) for num in winning_nums_str.split())
        my_nums = set(int(num) for num in my_nums_str.split())
        return Card(winning_nums, my_nums)
    
    @cached_property
    def number_of_matching_nums(self):
        return len(self.winning_nums & self.my_nums)

    @cached_property
    def score(self):
        if self.number_of_matching_nums > 0:
            return 2**(self.number_of_matching_nums-1)
        else:
            return 0 


def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        cards = [Card.from_str(line) for line in file.read().splitlines()]
    return cards

def star_02(cards: list[Card]) -> int:
    card_counts = [1 for card in cards]
    for i, card in enumerate(cards):
        for j in range(card.number_of_matching_nums):
            # Note i+j+1 < len(cards) always, according to problem statement
            card_counts[i+j+1] += card_counts[i]
    return sum(card_counts)


if __name__ == "__main__":
    timer = Advent_Timer()
    
    cards = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    star_01 = sum(card.score for card in cards)
    print(f"Star_01: {star_01}")
    timer.checkpoint_hit()
    
    print(f"Star_02: {star_02(cards)}")
    timer.checkpoint_hit()

    timer.end_hit()

from dataclasses import dataclass
from re import compile as compile_regex
from functools import cached_property
from aoc_tools import Advent_Timer

CARD_NUM_REGEX = compile_regex(r"Card\s+(?P<num>\d+)")

@dataclass
class Card:
    number: int
    winning_nums: set[int]
    my_nums: set[int]

    @staticmethod
    def from_str(card_str:str):
        card_num_str, numbers_str = card_str.split(": ")
        card_num = CARD_NUM_REGEX.match(card_num_str)["num"]
        winning_nums_str, my_nums_str = numbers_str.split(" | ")
        winning_nums = set(int(num) for num in winning_nums_str.split())
        my_nums = set(int(num) for num in my_nums_str.split())
        return Card(card_num, winning_nums, my_nums)
    
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
    card_counts = {card_num: 1 for card_num in range(len(cards))}
    for i, card in enumerate(cards):
        for j in range(i+1, min(i + 1 + card.number_of_matching_nums, len(cards))):
            card_counts[j] += card_counts[i]
    return sum(card_counts.values())


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

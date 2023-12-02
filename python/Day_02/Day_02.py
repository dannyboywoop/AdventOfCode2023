from dataclasses import dataclass, field
from aoc_tools import Advent_Timer
from re import compile as compile_regex

COLOUR_REGEX = compile_regex(r"(?P<quantity>\d+) (?P<colour>red|blue|green)")
GAME_REGEX = compile_regex(r"Game (?P<ID>\d+)")

@dataclass
class CubeSet:
    red: int = 0
    green: int = 0
    blue: int = 0

    @staticmethod
    def from_str(cubeset_str):
        cubset_dict: dict[str, int] = {}
        for colour_string in cubeset_str.split(", "):
            match = COLOUR_REGEX.match(colour_string)
            cubset_dict[match["colour"]] = int(match["quantity"])
        return CubeSet(**cubset_dict)
    
    def contained_in(self, other:"CubeSet"):
        return self.red <= other.red and self.blue <= other.blue and self.green <= other.green
    
    @property
    def power(self):
        return self.red * self.green * self.blue

@dataclass
class GameRecord:
    ID: int
    handfuls: list[CubeSet]

    @staticmethod
    def from_str(game_string):
        game_str, handfuls_str = game_string.split(": ")
        game_id = int(GAME_REGEX.match(game_str)["ID"])
        handfuls: list[CubeSet] = [CubeSet.from_str(handful_str) for handful_str in handfuls_str.split("; ")]
        return GameRecord(game_id, handfuls)

    def possible_with_bag(self, bag:CubeSet):
        for handful in self.handfuls:
            if not handful.contained_in(bag):
                return False
        return True
    
    def minimum_bag(self):
        min_red = max(handful.red for handful in self.handfuls)
        min_green = max(handful.green for handful in self.handfuls)
        min_blue = max(handful.blue for handful in self.handfuls)
        return CubeSet(red=min_red, green=min_green, blue=min_blue)

def read_data(input_file="input.txt"):
    with open(input_file, 'r') as file:
        games = [GameRecord.from_str(line.strip()) for line in file]
    return games

def star_01(games):
    bag = CubeSet(red=12, green=13, blue=14)
    return sum(game.ID for game in games if game.possible_with_bag(bag))

def star_02(games):
    return sum(game.minimum_bag().power for game in games)

if __name__ == "__main__":
    timer = Advent_Timer()
    
    games = read_data()
    print("Input parsed!")
    timer.checkpoint_hit()

    print(f"Star_01: {star_01(games)}")
    timer.checkpoint_hit()
    
    print(f"Star_02: {star_02(games)}")
    timer.checkpoint_hit()

    timer.end_hit()

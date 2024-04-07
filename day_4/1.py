import time
import pathlib
import pandas


def calculate_bingo_score(file_path: str):
    called_numbers, bingo_cards = _parse_bingo_game(file=file_path)
    print(f"{called_numbers=}")
    print(f"{bingo_cards=}")


def _parse_bingo_game(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        called_numbers = puzzle_input.readline().strip().split(",")
        puzzle_input.readline()
        blocks = puzzle_input.read().split("\n\n")
        cards: list[list[list[str]]] = list()
        for block in blocks:
            card = list()
            for line in block.splitlines():
                card.append(line.strip().split())
            cards.append(card)
        bingo_cards = list()
        for card in cards:
            bingo_cards.append(pandas.DataFrame(card, columns = [str(i + 1) for i in range(len(card))]))
        return called_numbers, bingo_cards


start = time.perf_counter()
print(calculate_bingo_score("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
# start = time.perf_counter()
# print(calculate_bingo_score("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

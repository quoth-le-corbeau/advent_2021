import time
import pathlib
import pandas


def calculate_power_consumption(file_path: str):
    diagnostic = _read_diagnostic(file=file_path)
    current_data_grid = diagnostic
    column_name = 1
    while len(current_data_grid) > 1 and column_name <= len(diagnostic.columns):
        oxygen_mode = _get_column_mode(
            column_name=column_name, data_grid=current_data_grid
        )
        oxygen_subset = current_data_grid[current_data_grid[column_name] == oxygen_mode]
        current_data_grid = oxygen_subset
        column_name += 1
    oxygen_generator_rating_string = "".join(
        [value for value in current_data_grid.values[0]]
    )
    oxygen_generator_rating = _binary_string_to_integer(
        binary_string=oxygen_generator_rating_string
    )
    print(f"{oxygen_generator_rating=}")


def _binary_string_to_integer(binary_string: str) -> int:
    order = len(binary_string)
    total = 0
    for i, char in enumerate(binary_string):
        total += 2 ** (order - (i + 1)) * int(char)
    return total


def _get_column_mode(column_name: int, data_grid: pandas.DataFrame) -> str:
    column_values = data_grid[column_name].values
    count_0 = 0
    count_1 = 0
    for value in column_values:
        if value == "0":
            count_0 += 1
        elif value == "1":
            count_1 += 1
        else:
            raise ValueError("Non-binary bit in column!")
    if count_0 <= count_1:
        return "1"
    else:
        return "0"


def _read_diagnostic(file: str) -> pandas.DataFrame:
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid = [list(line) for line in lines]
        return pandas.DataFrame(grid, columns=[i + 1 for i in range(len(lines[0]))])


start = time.perf_counter()
print(calculate_power_consumption("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
# start = time.perf_counter()
# print(calculate_power_consumption("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

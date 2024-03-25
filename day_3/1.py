import time
import pathlib
import pandas

# initialize list of lists
data = [['tom', 10], ['nick', 15], ['juli', 14]]
 
# Create the pandas DataFrame
df = pandas.DataFrame(data, columns=['Name', 'Age'])


def calculate_power_consumption(file_path: str):
    diagnostic = _parse_diagnostic(file=file_path)
    print(diagnostic)




def _parse_diagnostic(file: str):
    with open(pathlib.Path(__file__).parent / file, "r") as puzzle_input:
        lines = puzzle_input.read().splitlines()
        grid=[list(map(int, line)) for line in lines]
        print(f"{grid=}")
        return pandas.DataFrame(grid, columns=[i + 1 for i in range(len(lines[0]))])

start = time.perf_counter()
print(calculate_power_consumption("eg.txt"))
print(f"TEST -> Elapsed {time.perf_counter() - start:2.4f} seconds.")
# start = time.perf_counter()
# print(calculate_power_consumption("input.txt"))
# print(f"REAL -> Elapsed {time.perf_counter() - start:2.4f} seconds.")

import csv

def matrix_from_csv(file_name: str) -> list[list[float]]:
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        return [[float(num) for num in line] for line in reader]
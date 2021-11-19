import csv
from collections import defaultdict


def ReadCSV(filename: str):
    with open(filename, 'r', encoding='UTF-8') as f:
        total = defaultdict(int)
        while 1:
            line = f.readline()

            if not line:
                break

            for c in line:
                if ord(c) > 255:
                    print(c, end=": ")
                    print(ord(c))
                    total[c] += 1
        print(total)
    return
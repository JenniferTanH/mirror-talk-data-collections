import csv
from collections import defaultdict

csv_list = ["hp1.csv", "hp2.csv", "hp3.csv", "hp4.csv", "hp5.csv", "hp6.csv", "hp7.csv", "hp8.csv"]

def LineProcess(line: str):
    line = line.replace("\n", "")
    line = line.replace("’", "'")
    line = line.replace("“", "\"")
    line = line.replace("”", "\"")
    line = line.replace("…", "... ")
    line = line.replace("—", "")
    line = line.replace("\u2009", " ")
    line = line.replace("‘", "'")
    line = line.replace("[", "")
    line = line.replace("]", "")
    line = line.replace("–", ",")
    line = line.replace("9¾", "9 and 3/4")
    return line

def HarryCSV():
    csv_file = open("Harry.csv", 'a', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])
    for file in csv_list:
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[2]
                line = LineProcess(row[3])
                writer.writerow([name, line])


def DataProcess():
    with open("Harry.csv") as f:
        dict = defaultdict(int)
        while 1:
            line = f.readline()

            if not line:
                break

            for c in line:
                if ord(c) > 255:
                    dict[c] += 1
    print(dict)


def main():
    HarryCSV()
    DataProcess()


if __name__ == "__main__":
    main()

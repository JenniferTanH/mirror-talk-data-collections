import csv
from collections import defaultdict


def LineProcess(line: str):
    line = line.replace("\n", "")
    line = line.replace("’", "'")
    line = line.replace("“", "\"")
    line = line.replace("”", "\"")
    line = line.replace("…", "... ")
    line = line.replace(" —", ",")
    line = line.replace("–", ", ")
    line = line.replace("\u2009", " ")
    line = line.replace("‘", "'")
    line = line.replace("[", "")
    line = line.replace("]", "")
    return line


def DataProcess():
    with open("csv/DorseyCSV.csv") as f:
        count = 0
        # dict = defaultdict(int)
        while 1:
            line = f.readline()

            if not line:
                break
            if len(line) > 500:
                count += 1
    print(count)
    # print(dict)


def ReadData():
    csv_file = open("DorseyCSV4.csv", 'a', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])

    with open("data4.txt", 'r') as f:
        name = ""
        while 1:
            line = f.readline()

            if not line:
                break

            line = LineProcess(line)

            if len(line) < 2:
                continue

            name = line.split(":")[0]

            line = LineProcess(f.readline())
            if (name == 'Mr. Dorsey' or name == 'Jack Dorsey'):
                writer.writerow(['Dorsey', line])
            else:
                writer.writerow(['Interviewer', line])






def main():
    DataProcess()
    # ReadData()


if __name__ == "__main__":
    main()

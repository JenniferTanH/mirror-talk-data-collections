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
    with open("data3.txt") as f:
        dict = defaultdict(int)
        while 1:
            line = f.readline()

            if not line:
                break

            for c in line:
                if ord(c) > 255:
                    dict[c] += 1
    print(dict)


def ReadData():
    csv_file = open("DorseyCSV3.csv", 'a', encoding='utf-8')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])

    with open("data3.txt", 'r') as f:
        name = ""
        while 1:
            line = f.readline()

            if not line:
                break
            line = LineProcess(line)

            if len(line) < 2:
                continue
            arr = line.split(":  ")
            if(arr[0]!= "Ben" and arr[0] != "Jack"):
                if name == "Ben":
                    writer.writerow(["Interviewer", LineProcess(arr[0])])
                else:
                    writer.writerow(["Dorsey", LineProcess(arr[0])])
            else:
                name = arr[0]
                line = arr[1]
                if name == "Ben":
                    writer.writerow(["Interviewer", LineProcess(line)])
                else:
                    writer.writerow(["Dorsey", LineProcess(line)])




def main():
    # DataProcess()
    ReadData()


if __name__ == "__main__":
    main()

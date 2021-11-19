import csv
import os

Interviewee = "Kanye"
MAX_Length = 450


def CombineCSV():
    csv_list = os.listdir("csv")
    with open(Interviewee + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "line"])
        for file in csv_list:
            with open("csv/" + file, 'r') as d:
                reader = csv.reader(d)
                prev_name = ""
                for row in reader:
                    name = row[0]
                    if name == "name" or name == prev_name:
                        continue
                    prev_name = name

                    if len(row[1]) < 2:
                        continue
                    writer.writerow([name, row[1]])
                    # arr = SplitLine(row[1])
                    # for l in arr:
                    #     if len(l) > 2:
                    #         writer.writerow([name, l[0].upper() + l[1:]])
    return


def SplitLine(line):
    if len(line) < MAX_Length:
        return [line]
    else:
        idx = MAX_Length
        while idx < len(line):
            if line[idx] == '.':
                break
            idx += 1
        head = line[:idx + 1]
        tail = SplitLine(line[idx + 1:])
        return [head] + tail


def main():
    CombineCSV()


if __name__ == "__main__":
    main()

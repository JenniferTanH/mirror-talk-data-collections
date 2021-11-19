import csv
import os

Interviewee = "Snowden"
MAX_Length = 450

def CombineCSV():
    csv_list = os.listdir("csv")

    with open(Interviewee + ".csv", 'w') as f:
        writer = csv.writer(f)
        writer.writerow(["name", "line"])
        prev_name = ""
        for file in csv_list:
            with open("csv/" + file, 'r') as d:
                reader = csv.reader(d)
                for row in reader:
                    name = row[0]
                    if name == "name" or name == prev_name:
                        continue
                    # arr = SplitLine(row[1])
                    # for l in arr:
                    #     if len(l) > 2:
                    #         writer.writerow([name, l])
                    prev_name = row[0]
                    writer.writerow([row[0], row[1]])
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
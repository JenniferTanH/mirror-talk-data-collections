import csv
import os

Interviewee = "Tyson"
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
    # str = "Michelle,\"Well that was an act of complete frustration and desperation because I also talk about how I had tried it so may different ways. I had tried the part time situation when I was at the university and I first had Malia and I realised that part time work for professional women was it was an unequal trade off because I found that all I got was a part time salary. but I was still doing the same amount of work and still needed the same amount of babysitting so I was like, well that's a rip off for me so I tried that, then I was at the stage of trying - I was just so completely frustrated I had lost one of my best babysitters and I talk about the drama that happens when a working mother or mother of any kind loses their help and it's almost worse than being upset at your husband it's like 'you, I don't need the babysitter, I need her.\""
    # print(len(str))
    # arr = SplitLine(str)
    # print(len(arr))
    main()
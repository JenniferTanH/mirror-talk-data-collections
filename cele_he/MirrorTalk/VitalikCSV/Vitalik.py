import csv
import os
import re
import random

laughs = ['haha', 'hahaha']
NAME = ["Vitalik Buterin", "BUTERIN", "VITALIK BUTERIN", "A", "VB"]
Interviewee = "Vitalik"


def RandomReplace(arr):
    return arr[random.randint(0, len(arr) - 1)]


def LineProcess(line: str):
    # Basic process
    line = line.replace("\"", "")
    line = line.replace("\n", "")
    # ASCII process
    line = line.replace("’", "'")
    line = line.replace("“", "\"")
    line = line.replace("”", "\"")
    line = line.replace("″", "\"")
    line = line.replace("…", "... ")
    line = line.replace("– ", "")
    line = line.replace(" —", ",")
    line = line.replace("–", "-")
    line = line.replace("\u2009", " ")
    line = line.replace("‘", "'")
    line = line.replace("--", "")
    line = line.replace("  ", " ")
    # Special process
    line = line.replace("(LAUGHTER)", RandomReplace(laughs))
    line = line.replace("(LAUGH)", RandomReplace(laughs))
    line = line.replace("(laughter)", RandomReplace(laughs))
    line = line.replace("[laughs]", RandomReplace(laughs))
    line = line.replace("f***", "fuck")
    line = line.replace("f**k", "fuck")
    line = line.replace("s***", "shit")
    line = line.replace("s**t", "shit")
    # line 中所有符合正则表达式 r"\[.*\]" 的部分替换为 ""
    line = re.sub(r"\[.*\]", "", line)
    if len(line) > 1 and (line[-1] == ',' or line[-1] == ' '):
        line = line[:-1] + "."
    if len(line) > 1 and line[-1] != '.' and line[-1] != '?' and line[-1] != '!':
        line = line + "."
    return line


def LineSeperatedProcess(datafile, csvfile):
    csv_file = open("csv/" + csvfile, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])

    with open("data/Line-Sperated/" + datafile, 'r') as f:
        name = "Interviewer"
        while 1:
            line = f.readline()

            if not line:
                break

            line = LineProcess(line)

            if len(line) < 2:
                continue

            if name == "Interviewer":
                writer.writerow([name, line])
                name = Interviewee
            else:
                writer.writerow([name, line])
                name = "Interviewer"


def YoutubeProcess(datafile, csvfile):
    csv_file = open("csv/" + csvfile, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])

    with open("data/Youtube/" + datafile, 'r') as f:
        name = "Interviewer"
        while 1:
            line = f.readline().capitalize()

            if not line:
                break

            line += " " + f.readline()
            line += " " + f.readline()
            line += " " + f.readline()
            line += " " + f.readline()
            line += " " + f.readline()
            line = LineProcess(line)

            if len(line) < 2:
                continue

            if name == "Interviewer":
                writer.writerow([name, line])
                name = Interviewee
            else:
                writer.writerow([name, line])
                name = "Interviewer"


def QuestionSeperatedProcess(datafile, csvfile):
    csv_file = open("csv/" + csvfile, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])

    with open("data/Question-Mark-Seperated/" + datafile, 'r') as f:
        while 1:
            line = f.readline()

            if not line:
                break

            line = LineProcess(line)

            if len(line) < 2:
                continue

            if line[-1] == '?':
                writer.writerow(["Interviewer", line])
            else:
                writer.writerow([Interviewee, line])


def NameSeperatedProcess(datafile, csvfile):
    csv_file = open("csv/" + csvfile, 'w')
    writer = csv.writer(csv_file)
    writer.writerow(["name", "line"])
    with open("data/Name-Seperated/" + datafile, 'r') as f:
        name = "Interviewer"
        while 1:
            line = f.readline()

            if not line:
                break

            line = LineProcess(line)

            if len(line) < 2:
                continue

            arr = line.split(": ")

            if len(arr) < 2:
                if len(arr[0]) < 1:
                    continue
                if name in NAME:
                    writer.writerow([Interviewee, arr[0]])
                else:
                    writer.writerow(["Interviewer", arr[0]])
                continue
            name = arr[0]
            if name in NAME:
                writer.writerow([Interviewee, arr[1]])
            else:
                writer.writerow(["Interviewer", arr[1]])


def SpecialHandle():
    return -1


def CheckResult():
    csv_files = os.listdir("csv")
    for file in csv_files:
        with open("csv/" + file, 'r') as f:
            line = f.read()
            for c in line:
                if ord(c) > 255:
                    print(c, ord(c), file)


def main():
    line_seperated_file = os.listdir("data/Line-Seperated")
    for file in line_seperated_file:
        LineSeperatedProcess(file, file.replace(".txt", ".csv"))

    name_seperated_file = os.listdir("data/Name-Seperated")
    for file in name_seperated_file:
        NameSeperatedProcess(file, file.replace(".txt", ".csv"))

    quesion_seperated_file = os.listdir("data/Question-Mark-Seperated")
    for file in quesion_seperated_file:
        QuestionSeperatedProcess(file, file.replace(".txt", ".csv"))

    SpecialHandle()

    youtube_file = os.listdir("data/Youtube")
    for file in youtube_file:
        YoutubeProcess(file, file.replace(".txt", ".csv"))

    CheckResult()


if __name__ == "__main__":
    main()

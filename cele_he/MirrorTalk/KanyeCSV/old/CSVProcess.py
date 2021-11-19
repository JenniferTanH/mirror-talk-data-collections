import csv
import re
import random

name_set = ["Kanye West", "West", "MR. WEST", "KW"]
expected_name = ""
max_char = -1

affirmative = ['correct', 'positive', 'yes', 'yeah', 'that\'s right', 'agreed', 'affirmative']
laughs = ['lol', 'haha', 'hahaha']


def RandomReplace(arr):
    return arr[random.randint(0, len(arr) - 1)]


def NameProcess(name: str):
    if name in name_set:
        return expected_name
    return "Interviewer"


def LineProcess(line: str):
    # if line[0] == '"' and line[len(line) - 1] == '"':
    #     line = line[1:-1]
    line = line.replace("\n", "")
    line = line.replace("(affirmative)", RandomReplace(affirmative))
    line = line.replace("(Affirmative)", RandomReplace(affirmative))
    line = line.replace("(laughs)", RandomReplace(laughs))
    line = line.replace("(Laughs)", RandomReplace(laughs))
    line = line.replace("(Laughs.)", RandomReplace(laughs))
    line = line.replace("(Laughter.)", RandomReplace(laughs))
    line = line.replace("(Laugh)", RandomReplace(laughs))
    line = line.replace("[inaudible]", "")
    line = line.replace("(inaudible)", "")
    line = line.replace("(silence)", "")
    line = line.replace("(Inaudible.)", "")
    line = line.replace("(Inaudible) ", "")
    idx = 0
    while(idx < len(line) and line[idx] == ' '):
        idx += 1
    if(idx < len(line)):
        return line[idx:]
    else:
        return ""


def CSVProcess(name: str, data: str, max_char_input: int):
    # Set requirements
    global expected_name
    global max_char
    expected_name = name
    max_char = max_char_input

    # Open the CSV file
    file_name = "src/" + name + ".csv"
    csv_file = open(file_name, 'a', encoding='utf-8')
    writer = csv.writer(csv_file)

    # Writhe first row of the CSV file
    writer.writerow(["name", "line"])

    # Open the data source and keep reading
    with open(data, 'r') as data_file:
        while 1:
            line = data_file.readline()
            if line:
                # Regular Expression 表示 : + 任意数量空格
                arr = re.split(':\s*', line)
                # Means the line is empty, possibly "\n"
                if (len(arr[0]) <= 1):
                    continue

                char_name = NameProcess(arr[0])

                combined_line = ""
                total = 0
                for i in range(1, len(arr)):
                    combined_line += LineProcess(arr[i])
                    total += len(combined_line)

                if 1 < total < max_char:
                    writer.writerow([char_name, combined_line])

            # Can't read no more lines
            else:
                break
    return

def SpeechProcess(name: str, data: str, max_char_input: int):
    # Set requirements
    global expected_name
    global max_char
    expected_name = name
    max_char = max_char_input

    # Open the CSV file
    file_name = "src/" + name + ".csv"
    csv_file = open(file_name, 'a', encoding='utf-8')
    writer = csv.writer(csv_file)

    with open(data, 'r') as data_file:
        state = "name"
        name = ""
        while 1:
            line = data_file.readline()

            if not line:
                break

            if len(line) <= 1:
                continue

            if(state == "name"):
                name = NameProcess(line.split(":")[0])
                state = "line"
                # print("name is :", name)
                continue
            if(state == "line"):
                line = LineProcess(line)
                arr = re.split('\[.*\]', line)
                line = ""
                for l in arr:
                    line += l
                if 1 < len(line) < max_char:
                    # print("Result line is :", line)
                    writer.writerow([name, line])
                state = "name"
                continue




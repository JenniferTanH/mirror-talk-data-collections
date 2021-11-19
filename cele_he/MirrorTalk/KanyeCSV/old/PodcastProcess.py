import re
import csv



def PodcastProcess(interviewer: str, interviewee: str, filename: str):
    file_name = "src/" + interviewee + ".csv"
    csv_file = open(file_name, 'a', encoding='utf-8')
    writer = csv.writer(csv_file)

    writer.writerow(["name", "line"])

    with open(filename, 'r') as f:
        while 1:
            line = f.readline()

            if not line:
                break

            line = f.readline()
            print(line)
    return

import csv
import re

def WriteTXT(data):
    with open("data.txt", 'a') as f:
        for s in data:
            s = s + '\n'
            f.write(s)

def SentenceProcess(sentence: str):
    sentence = sentence.replace("\n", "")
    if len(sentence) > 2 and sentence[-1] != '.':
        sentence = sentence + '.'
    return sentence

def DataProcess(data: str, file: str, speaker1: str, speaker2: str):
    file_name = file
    csv_file = open(file_name, 'a', encoding='utf-8')
    writer = csv.writer(csv_file)

    # Writhe first row of the CSV file
    writer.writerow(["name", "line"])

    with open(data, 'r', ) as data_file:
        curr_speaker = 1
        while 1:
            line = data_file.readline()

            if not line:
                break

            arr = line.split('. ')

            for sentence in arr:
                if curr_speaker == 1:
                    writer.writerow([speaker1, SentenceProcess(sentence)])
                    curr_speaker = 2
                    continue
                if curr_speaker == 2:
                    writer.writerow([speaker2, SentenceProcess(sentence)])
                    curr_speaker = 1

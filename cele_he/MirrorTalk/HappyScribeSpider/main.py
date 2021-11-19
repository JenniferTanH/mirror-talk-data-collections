import DataProcess
import HappyScribeSpider
import SingleURLSpider
import sys

'''
Usage:
arg1: Where to store the data collected from Happyscribe
arg2: Where to store the csvfile cleaned from data
arg3: What to saerch in https://www.happyscribe.com/public
arg4: Name of the speaker1
agr5: Name of the speaker2

When any arg has a space in it, use double quotation mark.
eg: When try to search Kanye West, use "Kanye West" as arg3
'''
def main():
    # if len(sys.argv) != 6:
    #     print("Usage: \n"
    #           "arg1: Where to store the data collected from Happyscribe"
    #           "arg2: Where to store the csvfile cleaned from data"
    #           "arg3: What to saech in https://www.happyscribe.com/public"
    #           "arg4: Name of the speaker1"
    #           "agr5: Name of the speaker2")
    # data_path = sys.argv[1]
    # csv_name = sys.argv[2]
    # search = sys.argv[3]
    # speaker1 = sys.argv[4]
    # speaker2 = sys.argv[5]
    data_path = "data.txt"
    csv_name = "Vitalik.csv"
    search = "Vitalik+Buterin"
    speaker1 = "Interviewer"
    speaker2 = "Vitalik"


    #
    all_data = HappyScribeSpider.HappyScribeSpider(search)
    for data in all_data:
        DataProcess.WriteTXT(data)
        DataProcess.DataProcess(data_path, csv_name, speaker1, speaker2)


if __name__ == "__main__":
    main()
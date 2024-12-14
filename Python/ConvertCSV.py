import pandas as pd
import fileinput

def readCSV():
    data = pd.read_csv("/Users/sacjadha/Downloads/AR_Escalation_Statistics_Report.csv")
    return data


fieldNameMapping = {"Assigned To":"c4",   
 "Last Modified By":"c5",
 "Modified Date":"c6",
 "Status":"c7",
 "Escalation Name":"c8",
 "Status History":"c15",
 "Notifier Listening":"c16",
 "Record ID":"c379",
 "Actual Pool Number":"c59500",
 "Execution Count":"c59501",
 "Average Execution Time":"c59502",
 "Average Wait Time": "c59503",
 "Delayed By Statistics":"c59504",
 "Last Start Time":"c59505",
 "Last End Time":"c59506",
 "Escalation ID":"c59507",
 "Request ID":"c1",
 "Submitter":"c2",
 "Create Date":"c3"}
def updateCSVHeader():
    for line in fileinput.input("/Users/sacjadha/Downloads/AR_Escalation_Statistics_Report.csv",inplace=True):
        if fileinput.isfirstline():
            print(line)
            for k in fieldNameMapping:
                line.replace(k,fieldNameMapping[k])
                #return


def main():
    #data = readCSV()
    updateCSVHeader()
    #print(data.head())

if __name__ == '__main__':
    main()

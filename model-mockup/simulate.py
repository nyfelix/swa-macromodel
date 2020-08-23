import csv

dataDir = '/rea-data/'
dummyDataInput = 'dummy-data.csv'
dummyDataOutput = 'dummy-results.csv'

def createDummyResults():
    res = []
    with open(dataDir + dummyDataInput) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if len(row) > 0:
                res.append(float(row[0])*float(row[1]))
    with open(dataDir + dummyDataOutput, mode='w') as out_file:
        out_writer = csv.writer(out_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for val in res:
            out_writer.writerow([val])

if __name__ == "__main__":
    createDummyResults()
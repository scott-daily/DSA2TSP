import csv

def import_distance():
    distance_list = []

    with open('./documents/package_list.csv','r',encoding='utf-8', errors='ignore') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        for row in readCSV:
            distance_list.append(row)

        return distance_list



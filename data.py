import csv

def import_packages():
    package_list = []

    with open('./documents/package_list.csv','r',encoding='utf-8', errors='ignore') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        for row in readCSV:
            package_list.append(row)

        return package_list

def import_distances():
    distance_list = list(csv.reader(open('./documents/distance_table.csv')))
            
    return distance_list

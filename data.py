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

    #with open('./documents/distance_table.csv',encoding='utf-8', errors='ignore') as csv_file:
    #   readCSV = csv.reader(csv_file, delimiter=',')
    #    row_list = []
    #    for row in readCSV:
    #        for distance in row:
    #            row_list.append(distance)
        
    #    distance_list.append(row_list)
    #    row_list = []
            
    return distance_list

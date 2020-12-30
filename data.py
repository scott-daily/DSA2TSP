import csv
# This is a method used to import the package CSV information.  It goes through each row and creates a list out of each one.
# It's time complexity is O(N) and space complexity is also O(N).
def import_packages():
    package_list = []

    with open('./documents/package_list.csv','r',encoding='utf-8', errors='ignore') as csv_file:
        readCSV = csv.reader(csv_file, delimiter=',')
        for row in readCSV:
            package_list.append(row)
            
        return package_list
# This is similar to the above method, except it imports the distance information as a list of lists.
# It's time compexity is O(N) and space complexity is also O(N).
def import_distances():
    distance_list = list(csv.reader(open('./documents/distance_table.csv')))

    return distance_list

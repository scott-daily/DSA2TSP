from HashTable import HashTable
from Package import Package
from data import import_distance


#print(packages[7]['packageId'])
#packages[7]['packageLocation'] = 'On the truck'
#print(packages[7]['packageLocation'])

dist_list = import_distance()
packages = HashTable(41)

for item in dist_list:
    print(item[0])
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

print(packages[1].packageView())




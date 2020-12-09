from hashtable import HashTable
from package import Package
from data import import_packages, import_distances
from graph import Graph, Vertex


#print(packages[7]['packageId'])
#packages[7]['packageLocation'] = 'On the truck'
#print(packages[7]['packageLocation'])

# Use the import_packages function to transfer CSV package data into a python list.
package_list = import_packages()

# Initiate custom hash table with 41 slots
packages = HashTable(41)

# Use the import_distances function to transfer CSV distance data into a list of list
distance_table = import_distances()

# Create a dictionary to map addresses to their indexes for readability
dist_map = {'HUB': 0,'1060 Dalton Ave S': 1, '1330 2100 S': 2, '1330 2100 S': 3, '177 W Price Ave': 4, '195 W Oakland Ave': 5, '2010 W 500 S': 6,
                        '2300 Parkway Blvd': 7, '233 Canyon Rd': 8, '2530 S 500 E': 9, '2600 Taylorsville Blvd': 10, '2835 Main St': 11, '300 State St': 12,
                        '3060 Lester St': 13, '3148 S 1100 W': 14, '3365 S 900 W': 15, '3575 W Valley Central Station bus Loop': 16, '3595 Main St': 17, 
                        '380 W 2880 S': 18, '410 S State St': 19, '4300 S 1300 E': 20, '4580 S 2300 E': 21, '5025 State St': 22, '5100 South 2700 West': 23, 
                        '5383 South 900 East +ACM-104': 24, '600 E 900 South': 25, '6351 South 900 East': 26}

#print(distance_table)

# Iterate through each list the imported list of Packages.  
# Initiate a new package with the associated values and then insert that into the custom packages hash table.
for item in package_list:
    package = Package(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
    packages.insert(package['packageId'], package)

#Use Package class method to view the package contents
#print(packages[1].packageView())

# Print out the distance between two addreses using the dist_map address keys rather than dealing with numbers
print(distance_table[dist_map['HUB']][dist_map['3148 S 1100 W']])

#Create a new graph to use
city_graph = Graph()

#Convert the keys in the dist_map into a list of addresses
city_list = list(dist_map.keys())
print(city_list)

# Iterate through the addresses in the dist_map key values and add them to the city graph
for address in dist_map.keys():
    city_graph.add_address(address)

# Iterate through the dist_map with two loops, O(N^2) time.
# Add all the weighted edges between each address and the distance between them from the distance table.
for i in range(len(dist_map)):
    for j in range(len(dist_map)):
        city_graph.add_edge(city_list[i],city_list[j],distance_table[i][j])



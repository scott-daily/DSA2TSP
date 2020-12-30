class Truck:
    # The init method is called when a Truck instance is initialized.  
    # It has a time complexity of O(1) and a space complexity of O(1).
    def __init__(self):
        self.packageList = []
    # This is a method used to load a package into a Truck instance's packageList.  
    # It has a time complexity of O(1) and a space complexity of O(1).
    def loadPackage(self, package):
        self.packageList.append(package)
    # This has the same as loadPackage, except it unloads a package.
    def unloadPackage(self, package):
        self.packageList.remove(package)

    # This is a Python 'magic method' that allows a Truck to be printed and tells Python what to print.
    # This has a time complexity of O(1) and space complexity of O(1).
    def __repr__(self):
        return str(self.packageList)
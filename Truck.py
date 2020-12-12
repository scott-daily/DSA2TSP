class Truck:
    def __init__(self):
        self.packageList = []

    def loadPackage(self, package):
        self.packageList.append(package)

    def unloadPackage(self, package):
        self.packageList.remove(package)


    def __repr__(self):
        return str(self.packageList)
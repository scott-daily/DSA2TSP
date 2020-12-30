# Custom Package class that represents a package and it's attributes.
class Package:
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, mass_kg):
        self.packageId = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zip_code
        self.deadline = delivery_deadline
        self.mass = mass_kg
        self.packageLocation = "At the hub"
        self.deliveryTime = None

    # This is a method to view a single package's current attributes.  It has a time complexity of O(1) and space complexity of O(1).
    def packageView(self):
        return {'packageId': self.packageId, 'address': self.address, 'city': self.city, 'state': self.state, 'zipcode': self.zipCode, 'deadline': self.deadline, 'mass': self.mass,
        'packageLocation': self.packageLocation,'deliveryTime': self.deliveryTime}

    # This is a method to set the location of a package object.  It has a time complexity of O(1) and space complexity of O(1).
    def setLocation(self, location):
        self.packageLocation = location
    # This is a method to get any specified attributes value.  It's time complexity is O(1) and space complexity is O(1).
    def get(self, attribute):
        return getattr(self, attribute)
    # This method overwrites one of Python's 'magic methods' to make the package object's attributes accesible through subscripting.  It has a time complexity of O(1) and space 
    # complexity of O(1).
    def __getitem__(self, attribute):
        return getattr(self, attribute)
    # This method overwrites another magic method.  This allows a packages attribute to be set with subscription of the key name to set the value.
    # The time complexity is O(1) and the space complexity is O(1).
    def __setitem__(self, attribute, newValue):
        return setattr(self, attribute, newValue)
    # This tells Python what to do when a Package instance is printed using the magic method 'repr'.  It has a time complexity of
    # O(1) and a space complexity of O(1).
    def __repr__(self):
        return "['" + str(self.packageId) + "'" + ", " + "'" + str(self.address) + "'" + ", " + str(self.city) + "'" + ", " + "'" + str(self.state) + "'" + ", " + "'" + str(self.zipCode) + "'" + ", " + "'" + str(self.deadline) + "'" + ", " + "'" + str(self.mass) + "'" + ", " + "'" + str(self.packageLocation) + "'" + ", " + "'" + str(self.deliveryTime)+ "']"



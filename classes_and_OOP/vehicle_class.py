""" There are websites such as http://www.vehix.com that provide information about
secondhand vehicles. Design a base class for vehicle with fields such as model year,
total mileage, Vehicle Identification Number (VIN), EPA class, EPA mileage, engine,
transmission, and options.
Design subclasses for car, truck, SUV, and minivan. Think about the specific fields
and methods required for the subclasses.
"""

class Vehicle(object):
     def __init__(self, model_year = " ", total_mileage = 0.0, vin = " ", drive_type = " "):
         self.model_year_str = model_year
         self.total_mileage_int = total_mileage
         self.vin_str = vin
         self.drive_type_str = drive_type

     def __str__(self):
         return  "{} | {} | {}| {}".format(self.model_year_str, self.total_mileage_int,
                                           self.vin_str, self.drive_type_str)
     def __repr__(self):
         return Vehicle.__str__

class Car(Vehicle):
    def __init__(self, model_year = " ", total_mileage = 0.0, vin = " ", drive_type = " ", car_make = " "):
        Vehicle.__init__(self,model_year, total_mileage, vin, drive_type)
        self.car_make_str = car_make
    def __str__(self):
        return Vehicle.__str__(self) + f"| {self.car_make_str}"

mercedez = Car("2012", 25.0, "MKO3-KRD", "Left-Wheel", "Mercedez")
print (mercedez)
print(isinstance(mercedez, Vehicle))



class Vehicle:

    def __init__(self, vehicle_make, model, vehicle_colour, seat_capacity, max_speed, max_fuel_tank_capacity, kms_full_tank, fuel_effic):
        #Set Variables
        self.vehicle_make = vehicle_make
        self.model = model
        self.vehicle_colour = vehicle_colour
        self.seat_capacity = seat_capacity
        self.max_speed = max_speed
        self.max_fuel_tank_capacity = max_fuel_tank_capacity
        self.kms_full_tank = kms_full_tank
        self.fuel_effic = fuel_effic
        #Changing variables
        self.remaining_fuel = self.max_fuel_tank_capacity
        self.kms_left_to_empty = self.kms_full_tank


    def __str__(self):
        return (f"Vehicle Make: {self.vehicle_make}\nVehicle Model: {self.model}\n" + 
        f"Vehicle Colour: {self.vehicle_colour}\nNumber of Seats: {self.seat_capacity}\nMaximum Speed: {self.max_speed}km/hr" +
        f"Fuel Tank Capacity: {self.max_fuel_tank_capacity}\nKilometres to empty: {self.kms_full_tank}\nFuel Efficiency: {self.fuel_effic}L/100km")

    def rev_engine(self):
        return "VRRRRRRMMMMMMMMM!!!!!"

    def refuel(self, fuel_added):
        if self.remaining_fuel + fuel_added >= self.max_fuel_tank_capacity:
            self.remaining_fuel = self.max_fuel_tank_capacity
            self.kms_left_to_empty = self.kms_full_tank
            return f"Remaining Fuel: {self.remaining_fuel:.0f}L\nKilometres to Empty: {self.kms_left_to_empty:.0f}km"
        else:
            self.remaining_fuel += fuel_added
            self.kms_left_to_empty += (fuel_added * 100)/self.fuel_effic
            return f"Remaining Fuel: {self.remaining_fuel:.0f}L\nKilometres to Empty: {self.kms_left_to_empty:.0f}km"

    def drive_car(self, kms_driven):
        fuel_used = kms_driven * (self.fuel_effic / 100)
        self.remaining_fuel -= fuel_used
        self.kms_left_to_empty -= kms_driven
        if self.remaining_fuel < 0.15 * self.max_fuel_tank_capacity:
            print("Your fuel tank is nearly empty. Please refuel!")
        return f"Fuel used: {fuel_used:.0f}L\nRemaining Fuel: {self.remaining_fuel:.0f}L\nKilometres to Empty: {self.kms_left_to_empty:.0f}km"


maddie_suzuki = Vehicle("Suzuki", "Vitara Sport", "Teal", "5", 210, 47, 758, 6.2)
print(maddie_suzuki)
print()
print(maddie_suzuki.rev_engine())
print()
print(maddie_suzuki.drive_car(15))
print()
print(maddie_suzuki.drive_car(650))
print()
print(maddie_suzuki.refuel(20))
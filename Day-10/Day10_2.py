#Self Parameter

# Define the Car class with a method to print car information
class Car:
    Model = 'Suv'  # Class attribute for the car model
    Color = 'Red'  # Class attribute for the car color

    # Method to print car information using instance attributes
    def car_info(self):
        print(f"{self.Model} is the Car Model and it's color is {self.Color}")

# Create an instance 'class_car' of the Car class
class_car = Car()

# Calling the method car_info() using the instance (uncommented line)
# class_car.car_info()

# Alternative way to call the method by directly passing the instance to the class
Car.car_info(class_car)

# Explanation:
# 'car_info' is an instance method, so it's usually called using an instance of the class.
# But we can also call it directly from the class by passing the instance as the argument.

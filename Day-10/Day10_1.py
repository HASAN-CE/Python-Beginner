#Class attribute Vs Instance attribute

#Define the Car class with three class variables
class Car:
    Model = 'Sedan'   # 'Model' is a class attribute, shared by all instances
    Color = 'Red'     # 'Color' is a class attribute, shared by all instances
    Price = 2500000   # 'Price' is a class attribute, shared by all instances

# Create an instance 'car_class' of the Car class
car_class = Car() 
car_class.Model = 'Suv'  # 'Model' is set as an instance attribute, unique to 'car_class'
# Print 'Model', 'Color', and 'Price' for 'car_class'
print(car_class.Model, car_class.Color, car_class.Price)

# Explanation:
# Instance attributes (e.g., 'Model') have preference over class attributes 
# when set at the instance level, meaning if you assign a value to 'Model' in the instance, 
# it will override the class attribute value for that instance.
  
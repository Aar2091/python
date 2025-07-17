class Vehicle:

    def __init__(self, color, brand):
        
        self.color = color
        self.brand = brand

modelone = Vehicle("blue", "BMW")

print("model color is: ",modelone.color)
print("model brand is: ",modelone.brand)
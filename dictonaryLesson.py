# create
car = {"brand": "VW", "model": "Tiguan", "cyear": 2019, "color": "black"}

print(car)

#print(car.keys())
#print(car.values())
#print(car.items())

# read
#print(car["model"])
#print(car["color"])

#for key in car.keys():
#    print(car[key])

#for value in car.values():
#    print(value)

#for key,value in car.items():
#    print(f"{key} -> {value}")

#if "brand" in car:
#    print("The key 'brand' is part of the cars dict!")

#if "VW" in car.values():
#    print("The value 'VW' is part of the cars dict!")

# update
# car["cyear"] = 2011
car.update({"cyear": 2011})

car["color"] = ["black", "blue"]

# car["ps"] = 135
car.update({"ps": 140})

car[7] = "test"

print(car)


# delete
# del car[7]
car.pop(7)
print(car)

car.popitem()
print(car)

car.clear()
print(car)
'''
Lecture 4: Dictionary and Tuple
'''
my_tuple = "a", "b", "c", "d", "e"
print(my_tuple)
my_2nd_tuple = ("a", "b", "c", "d", "e")
print(my_2nd_tuple)
is_a_tuple = ("a",)
print(is_a_tuple)
print(my_tuple[1:3])
print(my_tuple[2:])
my_car = {"color":"red",
          "maker":"Toyota",
          "year":2015}
print(my_car)
print(my_car["color"])
print(my_car["year"])
print(my_car.items())
print(my_car.keys())
print(my_car.values())
print(my_car.get("year"))
my_car["model"]="Corolla"
print(my_car)
my_car["year"]=2020
print(my_car)
print(len(my_car))
print("year" in my_car)
print("Honda" in my_car)
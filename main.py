# 2.
my_dict = {"Kirill": 2007, "Egor": 2012, "Irina": 1986}
print(my_dict)
print(my_dict.get("Egor"))
my_dict["Karina"] = 1990
print(my_dict)
my_dict.update({"Gloria": 1965, "Ben": 1980})
print(my_dict)
a = my_dict.pop("Ben")
print(my_dict)
print(a)
# 3.
my_set = {True, False, True, 8, 7, 6, 7}
print(my_set)
print(my_set.add (9))
print(my_set.discard(8))
print(my_set)

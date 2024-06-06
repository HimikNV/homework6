my_dict = {"Mark": 1999, "Alex": 2001, "Alina": 2002,"Diana": 1998}
print(my_dict)
print(my_dict.get("Alex"))
print(my_dict.get("Sasha"))
my_dict.update({"Max": 1997,
                "Leonid": 1995})
a = my_dict.pop("Mark")
print(a)
print(my_dict)

my_set = {1 , 2, 1, 2, 3,3, 5, "String", "String", False, True}
print(my_set)
my_set.add(6)
my_set.add((23,45,132))
my_set.remove("String")
print(my_set)

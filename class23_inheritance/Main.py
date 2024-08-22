from Module import Vehicle, Car, suv

vehicle1 = Vehicle('Bertram', 'Sports Fisherman', 1980)
# print(vehicle1)
# vehicle1.get_age()

car1 = Car('Ford', 'Prius', 2000, 2)
# print(car1)
# car1.get_age()
print(car1.person_space())

suv1 = suv('Ford', 'Explorer', 2020, 4, 3)
print(suv1)
suv1.get_age()
print(suv1.person_space)
print(suv1.cargo_person_ratio())

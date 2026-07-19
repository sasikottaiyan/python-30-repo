# def add_ten():
#     ten = 10
#     def add(num):
#         return num + ten
#     return add

# # closure_result = add_ten()
# # print(closure_result(5))  # 15
# # print(closure_result(10))  # 20
# c=add_ten()
# print(c(10))


# numbers = [1, 2, 3, 4, 5] # iterable
# # def square(x):
# #     return x ** 2
# # numbers_squared = map(square, numbers)
# # print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# # Lets apply it with a lambda function
# numbers_squared = map(lambda x : x ** 2, numbers)
# print(list(numbers_squared))    # [1, 4, 9, 16, 25]


# numbers_str = ['1', '2', '3', '4', '5']
# converted = map(lambda x:int(x), numbers_str)
# print(list(converted))

#map()=====================================================================

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# upper=map(lambda x:x.upper(), countries)
# print(list(upper))

# sqaured=map(lambda x:x**2,numbers)
# print(list(sqaured))

#filter()==================================================
 
def land(countries):
    if "land" in countries:
        return True
    return False

land_names=filter(land,countries)
print(list(land_names))


#functions================================

# def add(a,b):
#     add = a+b
#     return add
# print(add(5,5))


# a=10
# b=20
# if(a!=10):
#     print(add(a,b))
# else:
#     print(add(a=50,b=50))

#level1==============================

# def add_two_numbers(a,b):
#     return a+b
# print(add_two_numbers(5,5))


# def area_of_circle(r):
#     area=3.14*r*r
#     return area
# print(area_of_circle(2))


# def add_all_nums(*num):
#         total=0
#         for i in num:
#             if isinstance(i, (int, float)):
#                 total+=i
#             else:
#                 print("parameter should be numbers")
#                 return None
#         return total
# print(add_all_nums(4,5,7))


# def convert_celsius(c):
#     faren=(c*9/5)+32
#     return faren
# print(convert_celsius(7))


# def check_season(month):
#     if month in("sept","nov"):
#         print('autum')
#     elif month in ("dec","jan","feb"):
#         print("winter")
#     elif month in ("june","july","august"):
#         print("spring")
#     elif month in ("oct","nov","mar"):
#         print("summer")
#     return month
# print(check_season("sept"))


# def print_list(my_list):
#     for i in my_list:
#         print(i)
# print(print_list([1,2,3,4]))


# def reverse_list(array):
#     empty=[]
#     for i in reversed(array):
#         empty.append(i)
#     return empty
# print(reverse_list((1,"e",5)))


# def capitalize_list_items(list):
#     for i in list:
#         print(i.upper())
# print(capitalize_list_items(["he","l"]))



# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# def add_item(add):
#     for i in add:
#         food_stuff.append(i)
#     return food_stuff
# print(add_item(['avacado','apple']))

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
def remove_item(remove):
    for i in remove:
        food_stuff.remove(i)
    return food_stuff
print(remove_item(['Tomato']))


    









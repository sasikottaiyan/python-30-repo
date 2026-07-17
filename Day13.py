#lambda functions===================

# numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
# seperate=[i for i in numbers if i<=0 ]
# print(seperate)


# list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# flatten=[j for i in list_of_lists for j in i]
# print(flatten)


# list_to_tuple= [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
# change= [ (i) for i in range(list_to_tuple)]
# print(change)


# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# flattened=[[country.upper(),country[:3],state.upper()]
# for [(country,state)] in countries]
# print(flattened)


# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# flattened=[{'country':country.upper(),'city':city.upper()}
#            for[(country,city)] in countries]
# print(flattened)


names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
combined=[]
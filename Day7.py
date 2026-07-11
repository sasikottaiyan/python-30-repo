#Sets===================

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

#level 1 ============

# print(len(it_companies))
# add=(it_companies.add("twitter"))
# print(it_companies)
# multi=(it_companies.update(["Nvdia","Shell"]))
# print(it_companies)
# remove=it_companies.remove("twitter")
# print(it_companies)

#level2================

# union= A.union(B)
# print(union)
# intersect=A.intersection(B)
# print(intersect)
# check1= A.issubset(B)
# print(check1)
# chcek2= A.isdisjoint(B)
# print(chcek2)

# print(A.union(B))
# print(B.union(A))

# sdiff=A.symmetric_difference(B)
# print(sdiff)
# del it_companies

#Level3========================

# set1=set(age)
# print(set1)
# print(len(set1))
# print(len(age))
# compare=len(set1)==len(age)
# print(compare)

# if len(set1) > len(age):
#     print("set is greater")
# else:
#     print("list is greater")

   
sentence="I am a teacher and I love to inspire and teach people"
split=sentence.split()
print(split)
convert_set= set(split)
print("unique words:",convert_set)
count_unique=len(convert_set)
print(count_unique)

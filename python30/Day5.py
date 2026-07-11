# list_1=["hello",5,6,7,8]
# print(len(list_1))
# print(list_1[0::2])
# mixed_data=[{'name':'sasi','age':20,'height':5.8}]
# print(mixed_data)


# it_companies=["facebook","IBM","apple","oracle","amazon"]
# print("no.of.comapnies:",len(it_companies))
# print(it_companies[0::2])
# it_companies[1]="wipro"
# print(it_companies)
# it_companies.insert(3,"toyota")
# print(it_companies)
# print(it_companies[-1].upper())
# print(it_companies)
# add=it_companies.append("#")
# print(it_companies)
# checkin="facebook" in it_companies
# print(checkin)
# asecending=it_companies.sort()
# print(it_companies)
# reverseing=it_companies.sort(reverse=True)
# print(it_companies)
# sliced=it_companies[0:3]
# print(sliced)
# del_first=it_companies.pop(0)
# print(it_companies)
# del it_companies
# print(it_companies)



# front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node','Express', 'MongoDB']
# joined=front_end+back_end
# print(joined)
# full_stack=joined
# print("full",full_stack)
# full_stack[5:5]=["python","sql"]
# print(full_stack)


#level 2 ======================

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

temp=ages.sort()
print(ages)
print("min_age:",min(ages))

temp2=ages.sort(reverse=True)
print(ages)
max_age=ages[0]
print("max_age:",max_age)

temp3=sum(ages)/len(ages)
print("avg:",temp3)

temp4=max(ages)-min(ages)
print("max,min:",temp4)

temp5=abs(temp2-temp3)==abs(temp2-temp3)
print("compare:",temp5)
#Dictionaries=============

dog={'name':'jacky','color':'orange','breed':'indian','legs':'4','age':'6'}

Student={'f_name':'sasi','l_name':'kottaiyan','age':'20','gender':'male','skills':['python','html']}
print('len_stu:',len(Student))

# get_value=Student.get('skills')
# print(get_value)
# print('type:', type(get_value))

# modify=Student['l_name']="kumar"
# append=Student['skills'].append('java')
# new_iteam=Student['work']='unemployed'
# print(Student)

key_list=list(Student.keys())
print(key_list)

values_list=list(Student.values())
print(values_list)

to_tuple=Student.items()
print(to_tuple)

del Student['l_name']
print(Student)

del dog
print(dog)
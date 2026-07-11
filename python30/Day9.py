#Condional Statements =====================================
 #level 1==========
# user=int(input("enter your age:"))
# if(user >= 18):
#     print("You are old enough to drive")
# else:
#     print(" wait for the missing amount of years")


# my_age=20
# your_age=int(input("enter ur age:"))
# if(my_age > your_age):
#     diff= abs(your_age- my_age)
#     if(diff==1):
#         print(" you are 1 year younger than me")
#     else:
#         print("you are",diff,"years younger than me")
# elif(my_age < your_age):
#     diff= abs(your_age - my_age)
#     if(diff==1):
#         print(" you are 1 year older than me")
#     else:
#         print("you are",diff,"years older than me")
# else:
#     print("we both at the same age")


# a= int(input("enter num1:"))
# b= int(input("enter num2:"))
# if(a > b):
#     print("a is greater")
# elif(a < b):
#     print("a is smaller than b")
# else:
#     print(" a is eqaul to b")
   
#Level2=================================

# score= int(input("enter your score:"))
# if(score >= 90 ):
#     print("A")
# elif(score >=80 and score <=89):
#     print("B")
# elif(score >=70 and score <=79):
#     print("C")
# elif(score >=60 and score <=69):
#     print("D")
# elif(score >=0 and score <=59):
#     print("F")


# season=input("enter the month:")
# if season in ("Sept" , "Oct" , 'Nov'):
#     print("Autumn")
# elif season in ("Dec","jan","feb"):
#     print("winter")
# elif season in( 'mar','april','may'):
#     print("spring")
# elif season in( 'june','july','august'):
#     print("summer")
# else:
#     print("enter correct season")

#Level 3 =========================================
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

# if("skills" in person):
#     check_skill=person["skills"]
#     middle= len(check_skill)//2
#     print("middle skills:",check_skill[middle])
# else:
#     print("no skills")


# if("skills" in person):
#     if("Python" in person["skills"]):
#         print("python is in skills")
#     else:
#         print("not in skills")


if person('skills') in {"javascript" , "React"}:
    print("he is front end developer")
elif person('skills') in {'Node', 'Python', 'MongoDB'}:
    print("he is abckend developer")
elif person("skills") in {"React","Node","MangoDB"}:
    print("hes fullstack")
else:
    print("unknown title")
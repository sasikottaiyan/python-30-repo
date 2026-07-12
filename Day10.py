#Loops ================

# count = 0
# while count < 5:
#     print(count)
#     count = count + 1
# else:
#     print(count)

# count = 0
# while count < 5:
#     if count == 3:
#         count += 1    
#     print(count)
#     count +=1

# language = 'Python'
# for i in range(len(language)):
#     print(language[i])

#level 1=============================

# n=10
# for i in range(n+1):    #for
#     print(i)
    
# n=0
# while n<11:             #while
#     print(n)
#     n +=1

# n=0
# for i in range(10,n-1,-1):  #for
#     print(i)

# count=10
# while count>=0:               #while
#     print(count)
#     count -=1


# count=1
# while count<=7:                #while
#     print("#"*count)
#     count +=1
    
# n=8
# for i in range(n):
#     for j in range(n):
#         print("#",end="")       #for 
#     print()


# n=0
# for i in range(11):
#     print(f"{i}*{i}={i*i}")
#     n +=1


# skills=['Python', 'Numpy','Pandas','Django', 'Flask']
# for skill in skills:
#     print(skill)


# n=100
# for i in range(n+1):
#     if i%2==0:
#         print(i)
#     else:
#         continue


# n=100
# for i in range(n+1):
#     if i%2 !=0:
#         print(i)
    

#level2 ===============================

# n=100
# total=0
# for i in range(n+1):
#     total +=i
# print("The sum of all numbers is:",total)


# n=100
# total_even=0
# total_odd=0
# for i in range(n+1):
#     if i%2==0:
#         total_even+=i
#     elif i%2 !=0:
#         total_odd +=i

# print("The sum of all evens is:",total_even,"And the sum of all odds is:",total_odd)


#level 3===============================================================

# countries = [
#   'Afghanistan',
#   'Albania',
#   'Algeria',
#   'Andorra',
#   'Angola',
#   'Antigua and Barbuda',
#   'Argentina',
#   'Armenia',
#   'Australia',
#   'Austria',
#   'Azerbaijan',
#   'Bahamas',
#   'Bahrain',
#   'Bangladesh',
#   'Barbados',
#   'Belarus',
#   'Belgium',
#   'Belize',
#   'Benin',
#   'Bhutan',
#   'Bolivia',
#   'Bosnia and Herzegovina',
#   'Botswana',
#   'Brazil',
#   'Brunei',
#   'Bulgaria',
#   'Burkina Faso',
#   'Burundi',
#   'Cabo Verde',
#   'Cambodia',
#   'Cameroon',
#   'Canada',
#   'Central African Republic',
#   'Chad',
#   'Chile',
#   'China',
#   'Colombia',
#   'Comoros',
#   'Congo, Democratic Republic of the',
#   'Congo, Republic of the',
#   'Costa Rica',
#   "Côte d'Ivoire",
#   'Croatia',
#   'Cuba',
#   'Cyprus',
#   'Czech Republic',
#   'Denmark',
#   'Djibouti',
#   'Dominica',
#   'Dominican Republic',
#   'East Timor (Timor-Leste)',
#   'Ecuador',
#   'Egypt',
#   'El Salvador',
#   'Equatorial Guinea',
#   'Eritrea',
#   'Estonia',
#   'Eswatini',
#   'Ethiopia',
#   'Fiji',
#   'Finland',
#   'France',
#   'Gabon',
#   'Gambia',
#   'Georgia',
#   'Germany',
#   'Ghana',
#   'Greece',
#   'Grenada',
#   'Guatemala',
#   'Guinea',
#   'Guinea-Bissau',
#   'Guyana',
#   'Haiti',
#   'Honduras',
#   'Hungary',
#   'Iceland',
#   'India',
#   'Indonesia',
#   'Iran',
#   'Iraq',
#   'Ireland',
#   'Israel',
#   'Italy',
#   'Jamaica',
#   'Japan',
#   'Jordan',
#   'Kazakhstan',
#   'Kenya',
#   'Kiribati',
#   'Korea, North',
#   'Korea, South',
#   'Kuwait',
#   'Kyrgyzstan',
#   'Laos',
#   'Latvia',
#   'Lebanon',
#   'Lesotho',
#   'Liberia',
#   'Libya',
#   'Liechtenstein',
#   'Lithuania',
#   'Luxembourg',
#   'Madagascar',
#   'Malawi',
#   'Malaysia',
#   'Maldives',
#   'Mali',
#   'Malta',
#   'Marshall Islands',
#   'Mauritania',
#   'Mauritius',
#   'Mexico',
#   'Micronesia',
#   'Moldova',
#   'Monaco',
#   'Mongolia',
#   'Montenegro',
#   'Morocco',
#   'Mozambique',
#   'Myanmar',
#   'Namibia',
#   'Nauru',
#   'Nepal',
#   'Netherlands',
#   'New Zealand',
#   'Nicaragua',
#   'Niger',
#   'Nigeria',
#   'North Macedonia',
#   'Norway',
#   'Oman',
#   'Pakistan',
#   'Palau',
#   'Palestine',
#   'Panama',
#   'Papua New Guinea',
#   'Paraguay',
#   'Peru',
#   'Philippines',
#   'Poland',
#   'Portugal',
#   'Qatar',
#   'Romania',
#   'Russia',
#   'Rwanda',
#   'Saint Kitts and Nevis',
#   'Saint Lucia',
#   'Saint Vincent and the Grenadines',
#   'Samoa',
#   'San Marino',
#   'Sao Tome and Principe',
#   'Saudi Arabia',
#   'Senegal',
#   'Serbia',
#   'Seychelles',
#   'Sierra Leone',
#   'Singapore',
#   'Slovakia',
#   'Slovenia',
#   'Solomon Islands',
#   'Somalia',
#   'South Africa',
#   'South Sudan',
#   'Spain',
#   'Sri Lanka',
#   'Sudan',
#   'Suriname',
#   'Sweden',
#   'Switzerland',
#   'Syria',
#   'Tajikistan',
#   'Tanzania',
#   'Thailand',
#   'Togo',
#   'Tonga',
#   'Trinidad and Tobago',
#   'Tunisia',
#   'Turkey',
#   'Turkmenistan',
#   'Tuvalu',
#   'Uganda',
#   'Ukraine',
#   'United Arab Emirates',
#   'United Kingdom',
#   'United States',
#   'Uruguay',
#   'Uzbekistan',
#   'Vanuatu',
#   'Vatican City',
#   'Venezuela',
#   'Vietnam',
#   'Yemen',
#   'Zambia',
#   'Zimbabwe'
# ];

# for i in countries:
#     if "land" in i:
#         print(i)


# fruits= ['banana', 'orange', 'mango', 'lemon']
# for i in fruits:
#     print(fruits[::-1],end=" ")




print("Login page")
username= input("enter username: ")
password= int(input("enter password: "))

print("your acc created sucessfully!")
print("now login!")

username2= input("enter username: ")
password2= int(input("enter password: "))

if username == username2 and password == password2:
    print("logged in sucess")
else:
    print("invalid credantial")

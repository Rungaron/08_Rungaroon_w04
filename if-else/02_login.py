username = "admin"
passwoed = "12345678"
user_input = str(input("Enter your Username : "))
pass_input = complex(input("Enter your Password : "))
print(type(pass_input))

if user_input == "admin" and pass_input == "12345678":
     print("Login Success !!!")
else :
     print("Invalid Username or Password")     
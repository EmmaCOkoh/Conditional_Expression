# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#                         Print or assign one of two values based on a condition
#                         X if condition else Y

# num = int(input("Enter a whole number: "))
# print("Positive" if num > 0 else "Negative")
#
# num1 = int(input("Enter any whole number: "))
# print("Even" if num1 % 2 == 0 else "Odd")

# a = 6
# b = 7
#
# max_num = a if a > b else b
# min_num = a if a < b else b
# print(max_num)
# print(min_num)

# age = int(input("How old are you?: "))
# status = "You are an adult" if age >= 18 else "You are a child"
# print(status)

# temperature = 30
# temp = "It is hot outside" if temperature >= 20 else "Weather is decent enough"
# print(temp)

user_role = "admin"
access_level = "Full access" if user_role == "admin" else "Access denied"
print(access_level)
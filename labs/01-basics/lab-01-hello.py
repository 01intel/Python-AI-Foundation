# Lab 01 - Hello World + Input/Output + Basic Types

name = input("Enter your name: ").strip()
age = int(input("Enter your age: ").strip())

print("\n--- Result ---")
print(f"Name: {name} (type: {type(name)})")
print(f"Age : {age} (type: {type(age)})")

next_year_age = age + 1
print(f"Next year you will be {next_year_age}.")

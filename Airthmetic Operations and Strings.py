# For the Arithmetic operations we are using python console to assign variable

#Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

#There are 7 arithmetic operators in Python :

#Addition

age1 = 4
age2 = 5

print("Addition")
Plus_age = age1 + age2
print(Plus_age)
#Subtraction

print("Subtraction")
Subtraction = age1 - age2
print(Subtraction)

#Multiplication
print("Multiplication")
Multiplication = age1 * age2
print(Multiplication)
#Division

print("Division")
Division_age = age1/ age2
print(Division_age)
#Modulus

print("Modulus")
Modulus_age = age1 % age2
print(Modulus_age)

#Strings

FirstName = "Bilal"
LastName = "Saeed"

Name = FirstName + " " + LastName
print(Name)

Sentence = "I'm playing cricket"
print(Sentence[0])
print(Sentence[5])
print(Sentence[0:12])
print(Sentence[:-4])


#Placeholders in Strings

# Use '%' sign to tell that this is a placeholder
# Use 's' to tell that what type is it and where to go

Name2 = "John"
sent = "%s is 25 Years Old"
print(sent%Name2)
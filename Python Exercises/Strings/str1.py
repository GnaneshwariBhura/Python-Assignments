#Create 3 variables to store street, city and country, now create address variable to 
# store entire address. Use two ways of creating this variable, one using + 
# operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line


street=input()
city=input()
country=input()
adreess=""
adreess= street+ " " + city + " " + country  # By conactination
print(adreess)
address=f"{street} {city} {country}" #By using Format string
print(address)

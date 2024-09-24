# Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to


city=input()
if city in india:
    print("India")
if city in pakistan:
    print("Pakistan")
if city in bangladesh:
    print("Bangladesh")
    
# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

city1=input()
city2=input()
res = [city1,city2]
# print(res)
if city1 in india:
    if city2 in india:
        print("Both cities are in India")
    else:
        print("They don't belong to same country")
if city1 in pakistan:
    if city2 in pakistan:
        print("Both cities are in Pakistan")
    else:
        print("They don't belong to same country")
if city1 in bangladesh:
    if city2 in bangladesh:
        print("Both cities are in Bangladesh")
    else:
        print("They don't belong to same country")

    
    
    
    
    
    
    
    
    
    
    
    
    
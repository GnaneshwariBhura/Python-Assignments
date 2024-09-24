# Lets say you are running a 5 km race. Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for i in range(1,6):
    if i<5:
        print("Are you tired?")
        ans=input()
        if ans=="yes":
            print("you didn't finish the race")
            break;
        if ans=="no":
            continue;
    if i==5:
        print("congratulations")

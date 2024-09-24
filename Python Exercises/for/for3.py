# Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.


#Using If condtion
expense_list = [2340, 2500, 2100, 3100, 2980]
n=int(input("Enter an expense amount: "))
if n in expense_list:
    if expense_list.index(n)+1==1:
        print("January")
    elif expense_list.index(n)+1==2:
        print("Febraury")
    elif expense_list.index(n)+1==2:
        print("March")
    elif expense_list.index(n)+1==2:
        print("April")
    elif expense_list.index(n)+1==2:
        print("May")
if n not in expense_list:
    print("Not found")
    

#Using for loop

expense_list = [2340, 2500, 2100, 3100, 2980]
n=int(input("Enter an expense amount: "))
if n in expense_list:
    for i in expense_list:
        if i==n:
            m=expense_list.index(n)+1
            if m==1:
                print("Jan")
            elif m==2:
                print("Feb")
            elif m==3:
                print("March")
            elif m==4:
                print("April")
            elif m==5:
                print("May")
else:
    print("Not Found")

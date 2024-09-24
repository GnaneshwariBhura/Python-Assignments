#Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

l=[['Jan',2200],['Feb',2350] , ['Mar',2600] ,['April',2130] , ['May',2190]]
# l1=[2200,2350,2600,2130,2190]
print(l[0][1]-l[1][1])

#Find out your total expense in first quarter (first three months) of the year.
print(l[0][1]+l[1][1]+l[2][1])


#Find out if you spent exactly 2000 dollars in any month
if 2000 in l:
    print("Yes")
else:
    print("Not spent")


#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
l.append([["June",1980]])
print(l)


#You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list  based on this
l[3][1]=l[3][1]+200
print(l)















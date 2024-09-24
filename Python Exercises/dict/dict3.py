# Create a set which only contains unique sqaures from a given a integer list.
# integer = [1, -1, 2, -2, 3, -3]
# sq_set = {1, 4, 9}

integer = [1, -1, 2, -2, 3, -3]
sq_set=set()
for i in integer:
    sq=i*i
    sq_set.add(sq)
print(sq_set)
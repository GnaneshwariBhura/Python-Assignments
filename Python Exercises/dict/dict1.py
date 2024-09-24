# Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.
# Example :
#     integer = [0, 1, 2, 3, 4]
#     binary = ["0", "1", "10", "11", "100"]
#     binary_dict = {0:"0", 1:"1", 2:"10", 3: "11", 4:"100"}

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]
d=dict()
i=0
while i<len(integer):
    d[integer[i]] = binary[i]
    i+=1
print(d)
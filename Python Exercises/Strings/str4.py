#I have a string variable called s='maine 200 banana khaye'. 
# This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
# Replace incorrect words in original strong with new ones and print the new string. 
# Also try to do this in one line.

wrg_str='maine,200,banana,khaye'
crt_str='maine 10 samosa khaye'
s1=wrg_str.split(sep=",")  
s2=crt_str.split()  #converting the string into list so that we can replace
s1[1]=s2[1]   
s1[2]=s2[2]
print(" ".join(s1))   #joining them as a string

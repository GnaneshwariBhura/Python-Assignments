# Stock	Prices
# info	[600,630,620]
# ril	[1430,1490,1567]
# mtl	[234,180,160]

d={'info':[600,630,620],'ril':[1430,1490,1567], 'mtl':[234,180,160]}
d1=list(d.keys())
d2=list(d.values())
l=[]
for i in d2:
    j=0
    res=0
    while j<len(i):
        res+=i[j]
        j+=1
    l+=[res/len(i)]
l1=[]
k=0
for k in l:
    l1+=[round(k,2)]
print("enter the input:")
ans=input()
if ans=="print":
    m=0
    while m<len(d):
        print(d1[m] , "==>" , d2[m],"==>",l1[m])
        m+=1
if ans=="add":
    print("Enter the stock and price")
    stock=input()
    price=int(input())
    if stock in d1:
        print(d[stock])
        print(d[stock].append(90))
    else:
        d[stock]=[price]
        print(d)


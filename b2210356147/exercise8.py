i=input("Enter 10 numbers with spaces in between:")
strlist=i.split(" ")
intlist=[]
intlist=[int(i) for i in strlist]
print(intlist)
print(sum(intlist)/len(intlist))
minlist=intlist.copy()
maxlist=intlist.copy()
def min():
    if len(minlist)==1:
        print(minlist)
    else:
        if minlist[0]>>minlist[-1]:
            minlist.pop(0)
            return min()
        if minlist[0]<<minlist[-1]:
            minlist.pop(-1)
            return min()
def max():
    if len(maxlist)==1:
        print(maxlist)
    else:
        if maxlist[0]<<maxlist[-1]:
            maxlist.pop(0)
            return max()
        if maxlist[0]>>maxlist[-1]:
            maxlist.pop(-1)
            return max()
min()
max()
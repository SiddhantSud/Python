lst1=[]
def check(num):
    if num in lst1 :
        return True
    return False

n=int(input("Ener the number of elements in the ist"))
for i in range(0,n):
    ele=int(input())
    lst1.append(ele)

key=int(input("Enter the search element"))
res=check(key)
print(res)

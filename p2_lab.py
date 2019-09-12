list1=[]
def check(elem):
    if elem in list1:
        return True
    return False
       
    

n=int(input("enter the numbe rof elements in the list"))
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print (list1)
key=int(input("enter the  number to be searched "))
ans=check(key)
print(ans)


        
   
    
    
   
 

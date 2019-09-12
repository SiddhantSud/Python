def rev(s):
    s1=s
    s1.reverse()
    for i in s1:
        print(i,end=' ')
    s1.reverse()
    print()
    for i in s1:
        print(i[-1::-1],end=' ')
        
x=input("enter a string")
sst=x.split()
rev(sst)
                


          
               

def fib(n):
    if(n<=1):
        return n
    elif(n>1):
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("Enter the number of values")

if(n<0):
      print("Wrong number")
else:
      for i in range(n):
          print(fibonacci(i))
      

class student :
    def __init__(self):
        self.__id=None
        self.__age=None
        self.__marks=None

    def validatemarks(self):
        if(self.__marks<65 and self.__marks<100):
            return True
        else:
            return False

    def validateage(self):
        if(self.__age>20):
            return True
        else:
            return False

    def check_qualification(self):
        m=self.validatemarks()
        a=self.validateage()
        if(m==True and a==True):
            if(self.__marks>65):
                return True
            else:
                return False
        else:
            return False
        
    def setter(self):
        self.__marks=int(input("Enter your marks"))
        self.__age=int(input("Enter yout age"))
        self.__id= int(input("Enter you id"))

    def getter(self):
        print("Student ID= ",self.__id)
        print("Student age=",self.__age)
        print("Student marls=",self.__marks)
        if(self.check_qualification()==True):
            print("Qualified")
        else:
            print("Not Qualified")


s=student()
s.setter()
s.getter()
  
    

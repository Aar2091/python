class A:
    def __init__(self,a):
        self.a = a

    def  __lt__(self,other):
        if(self.a<other.a):
          return "ob1 is less then ob2"
        else:
          return "ob1 is less then ob2"

ob1 = A(2)
ob2 = A(3)
print("Passed Values :", ob1.a, ob2.a)
print(ob1 < ob2)

        

    

    
            
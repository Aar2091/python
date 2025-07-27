class MyClass:

   __privateVariable = 283739

   def privMeth(self):
       print("I'm inside a class called MyClass")

   def hello(self):
     print("Private Variable value:", MyClass.__privateVariable)
     


myobject  = MyClass()
myobject.hello()
myobject.privMeth()
    
    
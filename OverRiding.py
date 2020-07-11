class Parent(object): 
    def __init__(self):
        self.value = 4 
    
    def get_value (self):
         return self 

class Child(Parent):
    def __init__(self):
        self.value = 5
    def get_value(self):
         return self.value +1  

c = Child() 
print(c._base_get_value ())
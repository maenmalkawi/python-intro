# # data class : a class that contain only data (fields and attribute ) and no method 

# # models and library in python 

# class Pointer : 
#     def __init__(self , x , y ):
#         self.x = x
#         self.y = y
        
#     def __eq__(self, other) : # self is p1 and other is p2
#         return self.x ==other and self.y ==other
            
        
#     def __str__(self):
        
#         return f" x is {self.x} and y is {self.y}"
    
# p1 =Pointer (1,2) 
# print ('p1 :',p1 )   
# print ('p1 type ', type(p1))
# p2 = Pointer( 1, 2)
# print ('p2: ' , p2)
# print ('p2 type ', type(p2))
        
# print("check if T or F : ", p1 == p2)        

# # the result is false because the two object are not same , they are two different objects (p1 , p2)
# # and every object has its own memory location 

# print("check memory location p1 : " , id(p1))
# print("check memory location p2 : " , id(p2 ))


# # to solve this proplem we use the magic method  __eq__ to check if the two objects are the same or not 



# abstraction >>
# abc library >>

from abc import ABC , abstractmethod



class payment(ABC):
    
    @abstractmethod    


    def pay(self, amount):
        pass
    
    @abstractmethod
    
    def dep(self , amount):
        pass
class paypal(payment):
    
    def __init__(self , name) :
        self.name = name

    def __str__(self):
        
        return f" name : {self.name}"
    
    
    def pay(self, amount):
        print(f' you are trying to pay with paypal amount of {amount}')
        
    def dep(self, amount):
        print(f'you are trying to deposet with paypal amount of {amount} ')
class CreditCard(payment):
    
    def __init__(self , name ):
        self.name = name        
    
    def __str__(self) -> str:
        return f'name : {self.name}'
    
    def pay(self, amount):
        print(f'you are trying to pay with creditCard fromm {self.name} amount of {amount}')
    
    def dep(self, amount):
        print(f'you are trying to deposet in the account {self.name} amount of {amount} ')    

pay2 = paypal('ahmad')        
pay2.pay(100)
 
 
credit1 = CreditCard('ahmad')
credit1.dep(200)            




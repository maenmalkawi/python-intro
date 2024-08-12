#multy inheretance : class can inheretance from more than one class 


class Grandfather :
    def __init__(self, family,city):
        self.family = family
        self.city=city
        
class Father:
    def __init__(self,name,age,job, family):
        # super().__init__(family)   
        self.name=name
        self.age=age
        self.job=job
class Mother:
    def __init__(self,eyesColor):
        self.eyesColor=eyesColor
                
class Son(Grandfather,Father,Mother):
    def __init__(self, name, age, job,Family,major,City,eyesColor):
      Grandfather.__init__(self,Family,City)
      Father.__init__(self, name, age,job)
      Mother.__init__(self,eyesColor)
      self.major=major
      
    def __str__(self):
          return f"name :{self.name} , age : {self.age} , job : {self.job} , major : {self.major}, family : {self.Family}, eyes : {self.eyesColor} , city : {self.City}"
      
son1 =Son('ahmad',20,'dev','se','family','blue','irbid')
print(son1)
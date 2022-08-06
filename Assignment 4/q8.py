class Person: 
      def __init__(self, first, last): 
          self.firstname = first 
          self.lastname = last 
      def __str__(self): 
          return self.firstname + " " + self.lastname 
 class Employee(Person): 
  def __init__(self, first, last, id): 
          super().__init__(first, last) 
          self.id = id 
  def __str__(self): 
          return super().__str__()+" "+self.id 
 x = Person("lovish", "sahil") 
 y = Employee("lovish", "sahil", "111") 
 print(x) 
 print(y) 
  
 """8)Output 
 lovish sahil  
 lovish sahil 111"""
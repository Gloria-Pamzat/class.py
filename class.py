class child:
    def_init_(self, firstname, lastname, grade, age):
    self.firstname = firstname
    self.lastname = lastname
    self.grade = grade
    self.age = age
    def firstname(self):
        return self_firstname
    def lastname(self):
        return self_lastname
    def grade(self):
        return self_grade
    def age(self):
        return self_age
        
        class teacher(child):
             def_init_(self, firstname, lastname, rank, age):
               super()._init_(firstname, lastname, grade, age)
                self.rank = rank
                
    child = child("joy", "manny", 200, 45)
    child1 = child("alfred", "paul", 300, 24)
    child2 = child("tracy", "josh", 14, 54)
    
    print(child.allInfo())
   
 

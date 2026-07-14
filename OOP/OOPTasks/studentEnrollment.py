#Code here
class Student:
  def __init__(self):
    self.__Std_id = None
    self.__age = None
    self.__Std_marks = None
  # setters
  def set_id(self,id):
    self.__Std_id = id 
  def set_age(self,age):
    self.__age = age 
  def set_marks(self,marks):
    self.__Std_marks = marks 
  # getters
  def get_id(self):
    return self.__Std_id
  def get_age(self):
    return self.__age
  def get_marks(self):
    return self.__Std_marks
  
  # data validation method 
  def data_validation(self):
    return True if self.__age > 20 and self.__Std_marks in range(0,101) else False
  def qualified(self):
    if self.data_validation():
      if self.__Std_marks >= 65:
        return True
      else:
        return False
    else:
      return False
    
# student 1
Std1 = Student()
Std1.set_id(1001)
Std1.set_age(21)
Std1.set_marks(85)
print("student id : {} , student_age : {} , student_marks : {}".format(Std1.get_id(),Std1.get_age(),Std1.get_marks()))
print("Data is valid " if Std1.data_validation() else "Data not valid ")
print("Student {}".format(Std1.get_id())," ",end='')
print("is qualified " if Std1.qualified() else "not qualified")
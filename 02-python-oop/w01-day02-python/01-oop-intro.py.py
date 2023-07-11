class Student:
    # CONSTRUCTOR
    def __init__(self,first_name,last_name,age,marks,fav_number):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.marks=marks
        self.fav_number=fav_number
    def increase_age(self):
        print("this is self: " , self)
        return None


john = Student("john","mayer",40,[12,45,32],23)


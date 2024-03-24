import random 
class Student:
    def __init__(self, ro,name, class_std, grade):
        self.name = name
        self.ro = ro
        self.class_std = class_std
        self.grade = grade


    def print_info(self):
        print("Ro : "+ str(self.ro) +"\nName : " + self.name + " \n" +"Class : "+ self.class_std + " \n" +"Grade : " + self.grade)




class School:
    std_obj = {}
 


    def enter_std(self, roll_number,name,grade,class_std):
        self.std_obj[roll_number] = Student(roll_number, name,class_std, grade)
        print("Stoerd")
    

    def get_std(self, roll_number):
        if roll_number in self.std_obj:
            self.std_obj[roll_number].print_info()
        else:
            print("Student not found")

    def rem_std(self, roll_number):
        if roll_number in self.std_obj:
            del self.std_obj[roll_number]
            print("Student removed")
        else:
            print("Student not found")





almurtaza = School()






def random_string(length):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    return ''.join(random.choice(letters) for i in range(length))




    
for i in range(10):
    almurtaza.enter_std(i,random_string(10), random_string(2), random_string(1))

for i in range(10):
    almurtaza.get_std(i)
    print(" --------------------------------")
print(dict(almurtaza.std_obj))
for i in range(10):
    almurtaza.rem_std(i)




print(dict(almurtaza.std_obj))

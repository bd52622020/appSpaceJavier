class Human():
    def __init__(self, firstname, lastname, university):
        self.firstname = firstname
        self.lastname = lastname
        self.university = university
    def __str__(self):
        return 'I am ' + self.firstname + self.lastname
        
        
class Student(Human):
    def __init__(self, firstname, lastname, university, skypeName):
        super().__init__(firstname, lastname, university)
        self.skypeName = skypeName
    def __str__(self):
        return Human.__str__(self) + ' and my skype name is ' + self.skypeName
        

class Researcher(Human):
    def __init__(self, firstname, lastname, university, subjects, phonenumber):
        super().__init__(firstname, lastname, university)
        self.subjects = subjects
        self.phonenumber = phonenumber
    def __str__(self):
        return Human.__str__(self) + ' and my phone number is' + self.phonenumber
    
human = Human('Javier', 'Sanchez', 'US')
print(human)

student = Student('Javier', 'Sanchez', 'US', 'a13sda')
print(student)

researcher = Researcher('Javier', 'Sanchez', 'US', ['mates'], '0754314343')
print(researcher)

    

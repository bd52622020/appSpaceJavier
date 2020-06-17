class UppercaseString():
    def __init__(self):
        self.string = ""
        
    def get_string(self, string):
        self.string = string
    
    def __str__(self):
        return self.string.upper()
    
# I think is a better option to intialize the attribute in the constructor
mystring = UppercaseString()
mystring.get_string("hello mates")
print(mystring)
        


class User:
    def showFullName(self):
        return self.userName + self.userFamily+self.userAge
    
    def __init__(self,userName,userFamily,userAge):
        self.userName = userName
        self.userFamily = userFamily
        self.userAge = userAge


sam = User("Sam","Azizi","39")
print(sam.showFullName())

class User2:
    def __init__(self,userName):
        self.user = userName
        self._password = "123456"
        self.__message = "I Love Python"
    def login(self,gotPass):
        if self._password == gotPass:
            print("user login") 
        else:
            print("pass incorrect")

me = User2("sam")
me.login('123456')
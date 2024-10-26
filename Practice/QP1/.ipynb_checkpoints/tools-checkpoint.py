from checker import InvalidInput
class Tools:
    def __init__(self,type="",strength=-1):
        self.__type = type
        self.__strength = strength

    @property
    def type(self):
        return self.__type

    @property
    def strength(self):
        return self.__strength
    
    @strength.setter
    def strength(self,strength):
        try:
            if(strength < 10 or strength > 20):
               raise InvalidInput("Strength does not meet parameters")
        except InvalidInput as i:
            print(i)
            
        else:
            self.__strength = strength
    
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self,type):
        self.__type = type
        
    def __str__(self):
        return "Type : "+str(self.__type)+" Strength : "+str(self.__strength)

def main():
    a = Tools()
    a.strength = 9
    print(a)

if __name__ =="__main__":
    main()

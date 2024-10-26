from tools import *
import pickle
class Spanner(Tools):
    def __init__(self,type="Spanner",strength=-1,size = -1):
        Tools.__init__(self,type,strength)
        self.__size = size

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self,size):
        try:
            if(size < 5 or size > 15):
               raise InvalidInput("Size does not meet parameters")
        except InvalidInput as i:
            print(i)
        else:
            self.__size = size
    def __str__(self):
        return Tools.__str__(self)+" Size : "+str(self.__size)

class ScrewDriver(Tools):
    def __init__(self,type="ScrewDriver",strength=-1,toothsize = -1):
        Tools.__init__(self,type,strength)
        self.__toothsize = toothsize

    @property
    def toothsize(self):
        return self.__toothsize
    
    @toothsize.setter
    def toothsize(self,toothsize):
        try:
            if(toothsize < 20 or toothsize > 40):
               raise InvalidInput("Toothsize does not meet parameters")
        except InvalidInput as i:
            print(i)
        else:
            self.__toothsize = toothsize
    def __str__(self):
        return Tools.__str__(self)+" ToothSize : "+str(self.__toothsize)

class Scissors(Tools):
    def __init__(self,type="Scissors",strength=-1,length = -1):
        Tools.__init__(self,type,strength)
        self.__length = length

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self,length):
        try:
            if(length > 12):
               raise InvalidInput("Length does not meet parameters")
        except InvalidInput as i:
            print(i)
        else:
            self.__length = length
    def __str__(self):
        return Tools.__str__(self)+" Length : "+str(self.__length)

def main():
    a = Scissors()
    a.length = 11
    #print(a)
    f = open("pickled.bin","rb")
    #pickle.dump(a,f)
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)
    print(x,"\n",y,"\n",z)
    
if __name__ =="__main__":
    main()

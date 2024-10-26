from toolkit import *
import csv
def main():
    flag = True
    loop = True
    tools = []
    while(loop):
        type = input("Enter tool type ")
        if type == "Spanner":
            i = Spanner()
            x1 = int(input("Enter strength : "))
            i.strength = x1
            if(i.strength != x1):
                break
            x2 = int(input("Enter size : "))
            i.size = x2
            if(i.size != x2):
                break 
            tools.append(i)
        elif type == "ScrewDriver":
            i = ScrewDriver()
            x1 = int(input("Enter strength : "))
            i.strength = x1
            if(i.strength != x1):
                break
            x2 = int(input("Enter toothsize : "))
            i.toothsize = x2
            if(i.toothsize != x2):
                break 
            tools.append(i)
        elif type == "Scissors":
            i = Scissors()
            x1 = int(input("Enter strength : "))
            i.strength = x1
            if(i.strength != x1):
                break
            x2 = int(input("Enter length : "))
            i.length = x2
            if(i.length != x2):
                break 
            tools.append(i)
        choice = input("Enter another tool? ")
        if(choice == 'n'):
            loop = False

    f = open("Tools.csv","w")
    for i in tools:
        writer = csv.writer(f)
        writer.writerow([i.type,i.strength])
            
if __name__ =="__main__":
    main()

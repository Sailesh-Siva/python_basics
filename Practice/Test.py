"""This is a text doct"""
import csv
def testing():
    f = open("csvfile.csv","r",newline="")
    l = [[1,"Sailesh"],[2,"Nigg"],[3,"Sus"]]
    reader = csv.reader(f)
    for i in reader:
        print(i)

def testing1():
    """for printing csv"""
    f = open("csvfile1.csv","r",newline="")
    #fields = ["id","name"]
    #d = [{"id":2,"name":"Sus"},{"id":4,"name":"Su "},{"id":7,"name":"S s"}]
    #writer = csv.DictWriter(f,fieldnames = fields)
    #writer.writeheader()
    #writer.writerows(d)
    reader = csv.DictReader(f)
    for i in reader:
        print(i)
    
def main():
    testing1()
if __name__ == "__main__":
    main()

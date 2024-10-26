from django.shortcuts import render

# Create your views here.
count = 0
val = -1
flag = 0
def home(request):
    return render(request,"home.html")
def getStudentDetails(request):
    global val
    global flag
    val = int(request.GET["no"])
    return render (request,"StudentDetails.html")

def createStudentObjs(request):
    global val
    global flag
    count+=1
    if count <= val:
        regno = request.GET["regno"]
        name = request.GET["name"]
        m1 = float(request.GET["m1"])
        m2 = float(request.GET["m2"])
        avg = (m1+m2)/2

        flag = 1
        return render(request,"StudentDetails.html",{'robj':rno,'nobj':name,'aobj':avg,flag:'flag'})


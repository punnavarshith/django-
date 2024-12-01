from django.shortcuts import render
from . models import Student
# Create your views here.
def home(request):
    if request.method == 'POST':
        StudentRegNumber = request.POST['StudentRegNumber']
        StudentName = request.POST['StudentName']
        NameOftheProgramme=request.POST['NameOftheProgramme']
        StudentAddress=request.POST['StudentAddress']
        ContactMobileNumber=request.POST['ContactMobileNumber']
        StatusOftheSemesterFee=True if  request.POST['StatusOftheSemesterFee']=='true' else False
        stud=Student(StudentRegNumber=int(StudentRegNumber), StudentName=StudentName, NameOftheProgramme=NameOftheProgramme, StudentAddress=StudentAddress, ContactMobileNumber=ContactMobileNumber, StatusOftheSemesterFee=StatusOftheSemesterFee)
        stud.save()
       
        return render(request,'home.html')
    return render(request,'home.html')

def status(request):
    allstudentsdetails=Student.objects.all()
    return render(request, 'status.html', {'allstudentsdetails': allstudentsdetails})
from django.shortcuts import render,get_object_or_404,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from .models import Student
from .forms import StudentForm

#api
from rest_framework.decorators import api_view # 1. API ki power dene wala decorator
from rest_framework.response import Response    # 2. JSON bhejne wala function
from .serializers import StudentSerializer      # 4. Tumhara Packing Machine

# Create your views here. get=ony one record filter=many records
def index(request):
    context={
        # 'student':Student.objects.filter(uni='uo')
        'student':Student.objects.all()
    }
    return render(request,'core/index.html',context)

def addimginform(request):
    if request.method == 'POST':
        name =request.POST.get("name")
        uni =request.POST.get("uni")
        su  =request.POST.get("sub")
        sem =request.POST.get("sem")
        img = request.FILES.get('project_image')
        Student.objects.create(name=name,uni=uni,subject=su,semester=sem, image=img)


#API integration..............
@api_view(['GET', 'POST']) # Ab ye GET aur POST dono lega
def student_list_api(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # 1. User ka bheja hua data serializer ko do
        serializer = StudentSerializer(data=request.data)
        # 2. Check karo ke data valid hai (e.g. name missing toh nahi?)
        if serializer.is_valid():
            serializer.save() # Database mein save kar do
            return Response(serializer.data, status=201) # Created
        return Response(serializer.errors, status=400) # Bad Request
    
#crud
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api(request, pk): # pk matlab Primary Key (ID)
    try:
        student = Student.objects.get(pk=pk) # Database mein wo ID dhoondo
    except Student.DoesNotExist:
        return Response({'error': 'Student nahi mila!'}, status=404)

    # 1. GET: Sirf us student ka data dikhao
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    # 2. PUT: Data update karo (Edit)
    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    # 3. DELETE: Student ko database se nikal do
    if request.method == 'DELETE':
        student.delete()
        return Response(status=204) # No Content (Success)

# API integration ends.....................

def base(request):
    return render(request,'core/base.html')

def stuent_details(request,student_id):
    try:
        # 1. Student dhoondne ki koshish karo
        stu = Student.objects.get(id=student_id)
        stu.delete()
        
        # 2. Agar delete ho jaye toh success message bhejo
        messages.success(request, "Student ka record kamyabi se delete ho gaya hai!")
            
    except Student.DoesNotExist:
        # 3. Agar ID database mein na ho, toh error message bhejo
        messages.error(request, "Error: Is ID ka koi student mojud nahi hai.")
        
    except Exception as e:
        # 4. Koi aur masla ho toh wo bhi pakar lo
        messages.warning(request, f"Kuch galat hua: {e}")
    return render(request,'core/dynamicurl.html',{'students':stu})

# forms
def add_student(request):
    if request.method == "POST":
        # Jab user button dabaye (Data bhej raha ho)
        form = StudentForm(request.POST) 
        if form.is_valid():
            form.save()  # Asali jadu! Database mein save ho gaya
            messages.success(request, "Student kamyabi se add ho gaya!")
            return redirect('home')  # Wapas main page par bhej do
    else:
        # Jab user pehli baar page kholay (Khali form chahiye)
        form = StudentForm()
        
    return render(request, 'core/forms.html', {'form': form})

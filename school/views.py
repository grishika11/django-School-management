from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from .models import Image,User,Teacher
from .forms import ImageForm, StudentForm,TeacherForm
import csv
import xlwt


# Create your views here.
def Home(request):
	return render(request,'home.html')

def Contact(request):
	return render(request,'Contact.html')

def About(request):
	return render(request,'about.html')


def Adminlog(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,user)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}    
    return render(request,'admin_login.html',d)



def Gallery(request):
    if request.method == "POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'gallery.html',{'img':img,'form': form})


def Logout(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('home')


def Upload(request):
    if request.method =="POST":
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    form = ImageForm()
    img = Image.objects.all()
    return render(request,'upload.html',{'img':img , 'form':form})

def delete_img(request,id):
    if request.method=='POST':
        img = Image.objects.get(pk=id)
        img.delete()
    return redirect('upload')

def Admission(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            clas = fm.cleaned_data['clas']
            city = fm.cleaned_data['city']
            reg = User(name=name,email=email,clas=clas,city=city)
            reg.save()

    else:
        fm = StudentForm()
    stud = User.objects.all()
    return render(request,'admission.html',{'form':fm,'stu':stud})

def Career(request):
    if request.method == 'POST':
        
        fv = TeacherForm(request.POST,request.FILES)
        if fv.is_valid():
            name = fv.cleaned_data['name']
            email = fv.cleaned_data['email']
            qly = fv.cleaned_data['qly']
            exp = fv.cleaned_data['exp']
            city = fv.cleaned_data['city']
            filepath = request.FILES['filepath']
            reg = Teacher(name=name,email=email,qly=qly,exp=exp,city=city,filepath=filepath)
            reg.save()

    else:
        fv = TeacherForm()
    stud = Teacher.objects.all()
    return render(request,'career.html',{'form':fv,'stu':stud})


def Career_view(request):
    fm = TeacherForm()
    stud = Teacher.objects.all()
    return render(request,'career_view.html',{'stu':stud})


def Student_view(request):
    fv = StudentForm()
    stud = User.objects.all()
    return render(request,'Student_view.html',{'stu':stud})

def delete_data_career(request,pk):
    pi = Teacher.objects.get(id=pk)
    if request.method =="POST":
        pi.delete()
        return redirect('career_view')
    context = {'pi':pi}
    return render(request,'deleteit.html',context)


def delete_data_admission(request,id):
    if request.method =="POST":
        pc = User.objects.get(pk=id)
        pc.delete()
        return redirect('student_view')

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content_Disposition']='attachment;filename=career'+'.csv'
    writer = csv.writer(response)
    writer.writerow(['name','email','qly','exp','city'])

    stud = Teacher.objects.all()

    for st in stud:
        writer.writerow([st.name,st.email,st.qly,st.exp,st.city])

    return response



def export_excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content_Disposition']='attachment;filename="career.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("career")
    row_num=0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns=['name','email','qly','exp','city']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    stud = Teacher.objects.all().values_list('name','email','qly','exp','city')

    for my_row in stud:
        row_num = row_num + 1
        for col_num in range(len(my_row)):
            ws.write(row_num, col_num, my_row[col_num], font_style)
      
    wb.save(response)
    return response



from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import AccountsModel
# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def sobang(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "국제소방교류협회"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'sobang.html')    
        else:
            return render(request,'sobang.html')    
    return render(request,'sobang.html')

@csrf_exempt
def dongpo(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "중국동포연합회"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'dongpo.html')    
        else:
            return render(request,'dongpo.html')    
    return render(request,'dongpo.html')

@csrf_exempt
def susanbangsong(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "수산방송"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'susanbangsong.html')    
        else:
            return render(request,'susanbangsong.html')    
    return render(request,'susanbangsong.html')

@csrf_exempt
def founder(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "예비창업자"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'founder.html')    
        else:
            return render(request,'founder.html')    
    return render(request,'founder.html')

@csrf_exempt
def iyousystemz(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "아이유시스템즈"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'iyousystemz.html')    
        else:
            return render(request,'iyousystemz.html')    
    return render(request,'iyousystemz.html')

@csrf_exempt
def student(request):
    account = AccountsModel()
    if request.method == "POST":
        if 'name' in request.POST:
                if 'check' in request.POST:
                    name = request.POST['name']
                    phonenumber = request.POST['phonenumber']
                    account.name = name
                    account.phonenumber = phonenumber
                    account.checkbox = "대학생"
                    account.save()
                    return render(request,'good.html')
                else:
                    return render(request,'student.html')    
        else:
            return render(request,'student.html')    
    return render(request,'student.html')

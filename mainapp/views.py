from django.shortcuts import render
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import AccountsModel
from .forms import AccountForm
# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def sobang(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'sobang.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "국제소방교류협회"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'sobang.html')

@csrf_exempt
def dongpo(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'dongpo.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "중국동포연합회"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'dongpo.html')

@csrf_exempt
def susanbangsong(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'susanbangsong.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "수산방송"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'susanbangsong.html')

@csrf_exempt
def founder(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'founder.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "예비창업자"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'founder.html')

@csrf_exempt
def iyousystemz(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'iyousystemz.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "아이유시스템즈"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'iyousystemz.html')

@csrf_exempt
def student(request):

    if request.method == "POST":
        form = AccountForm(request.POST)
        name = request.POST['name']
        phonenumber = request.POST['phonenumber']
        res_data = {}
        if not(name and phonenumber):
            res_data['error']="모든 칸을 다 입력해주세요."
            return render(request,'student.html')
        elif 'check' in request.POST:
            account = AccountsModel()
            account.name = name
            account.phonenumber = phonenumber
            account.checkbox = "대학생"
            account.save()
            return redirect('https://www.shinhancard.com/pconts/html/benefit/event/1198411_2239.html')
    return render(request,'student.html')
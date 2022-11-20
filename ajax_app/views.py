from django.http import JsonResponse
from django.shortcuts import render
from .models import studentmodel
from .forms import StudentRegistration 
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
      form=StudentRegistration()
      dtls=studentmodel.objects.all()
      context={'form':form,'dtls':dtls}
      return render(request,'home.html',context)

@csrf_exempt
def add_data(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            prnid = request.POST['personid']
            name = request.POST['name']
            age = request.POST['age']
            if(prnid == ''):
                prsn = studentmodel(name=name,age=age)
            else:
                prsn = studentmodel(id=prnid,name=name,age=age)
            prsn.save()
            x = studentmodel.objects.values()
            print(x)
            x_data = list(x)
            print("---")
            print(x_data)
            return JsonResponse({'terms':'add','x_data':x_data})
        else:
            return JsonResponse({'terms':0})      

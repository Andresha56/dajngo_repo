from django.shortcuts import redirect, render
from .models import Image
from .forms import Imageform

# Create your views here.


def index(request):
    if request.method=="POST":
        form=Imageform(request.POST,request.FILES)
        if form.is_valid():
            print('form validation ..')
            print('Name',form.cleaned_data['name'])   
            form.save()
            return redirect('homepage')
    else:
        form=Imageform
        print("get method is runing")
        
    img=Image.objects.all()
    param={'form':form,'img':img}
    return render(request,'index.html',param)
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from Phuc_App.forms import BaibaoForm
from Phuc_App.models import Baibao
# Create your views here.
def Create(request):
    if request.method == "POST":
        form = BaibaoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = BaibaoForm()
    return render(request,'index.html',{'form':form})

def index(request):
    articles = Baibao.objects.all()
    return render(request,"display.html",{'articles':articles})

def edit(request,id):
    articles = Baibao.objects.get(id=id)
    return render(request,'edit.html',{'articles':articles})

def update(request,id):
    articles = Baibao.objects.get(id=id)
    form = BaibaoForm(request.POST, instance = articles)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'edit.html',{'articles':articles})

def destroy(request,id):
    articles = Baibao.objects.get(id=id)
    articles.delete()
    return redirect("/")
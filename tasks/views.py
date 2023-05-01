from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
tasks = []
# Create your views here.
class manageform(forms.Form):
    task = forms.CharField(label = "AddTask",max_length=50)
   
    
def index(request):
    return render (request,"index.html",{
        "tasks":tasks,
        
    })
def add(request):
    if request.method == "POST":
        form = manageform(request.POST)
        if(form.is_valid()):
            task = form.cleaned_data["task"]
            
            tasks.append(task)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render (request,"add.html",{
        "form":manageform()
    })
    return render (request,"add.html",{
        "form":manageform()
    })
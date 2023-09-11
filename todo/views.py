from django.shortcuts import render, redirect
from .models import ToDo

def Home(request):
        if request.method == "POST":
        title = request.POST.get('title')
        if title != "":
            ToDo.objects.create(title=title)
        return redirect('home')

    data = ToDo.objects.all()
    data_cont = {"data": data}
    return render(request, 'home.html', data_cont)

def Delete(request, id=None):
    ToDo.objects.get(id=id).delete()
    return redirect('home')

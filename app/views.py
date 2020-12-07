from django.shortcuts import render
from app.forms import NewUser

# Create your views here.


def login(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            form.save(commit = True)
        else:
            print("form invalid")
            return 0
    return render(request,'app/login.html',context = {'form': form})

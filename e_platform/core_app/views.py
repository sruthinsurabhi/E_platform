from django.shortcuts import render,redirect
from items.models import Category, item
from .forms import SignupForm

def index(request):
    items = item.objects.filter(is_available=True)[0:6]
    categories = Category.objects.all()
    return render(request, 'core_app/index.html', {'items': items, 'categories': categories})

def contact(request):
    return render(request, 'core_app/contact.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:

        form=SignupForm()

    return render(request,'core_app/signup.html',{'form':form})

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core_app/index.html')
def contact(request):
    return render(request,'core_app/contact.html')
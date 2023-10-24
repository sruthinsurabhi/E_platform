from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from items.models import item
# Create your views here.


@login_required
def index(request):
    items=item.objects.filter(created_by=request.user)

    return render(request,'dashboard/index.html',{
        'items':items})

@login_required
def delete(request,pk):
    item=get_object_or_404(item,pk=pk,created_by=request.user)
    item.delete()


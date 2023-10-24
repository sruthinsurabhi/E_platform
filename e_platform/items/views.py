from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import item,Category
from django.db.models import Q
from .forms import NewItemForm,EditItemForm

# Create your views here.
def items_b(request):
    query=request.GET.get('query','')
    category_id=request.GET.get('category',0)

    categories=Category.objects.all()
    items=item.objects.filter(is_available=True)
    if category_id:
        items=items.filter(category_id=category_id)
    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))
    return render(request,'item/item.html',{'items':items,'query':query,
                                            'categories':categories,
                                            'category_id':category_id})



def detail(request,pk):
    items=get_object_or_404(item,pk=pk)
    related_items=item.objects.filter(category=items.category,is_available=True).exclude(pk=pk)[0:3]
    return render(request,'item/detail.html',{'item':items,'related_items':related_items})

@login_required
def new(request):
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)
        if form.is_valid():
            item=form.save(commit=False)
            item.created_by=request.user
            item.save()
            return redirect('item:detail',pk=item.id)
    else:

        form=NewItemForm()
    return render(request,'item/form.html',{'form':form,'title':'New Item'})

@login_required
def delete(request,pk):
    Item=get_object_or_404(item,pk=pk,created_by=request.user)
    Item.delete()
    return redirect('dashboard:index')

@login_required
def edit(request, pk):
    Item = get_object_or_404(item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=Item)  # Corrected 'Item' to have a capital 'I'
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=Item.id)  # Corrected 'Item' to have a capital 'I'
    else:
        form = EditItemForm(instance=Item)
    return render(request, 'item/form.html', {'form': form, 'title': 'Edit Item'})

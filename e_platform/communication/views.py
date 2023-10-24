from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Conversation,ConversationsMessage
from items.models import item as Item  
from communication.forms import ConversationForm

@login_required
def new_conversation(request, item_pk):
    target_item = get_object_or_404(Item, pk=item_pk)  

    if target_item.created_by == request.user:
        return redirect('dashboard:index')
    
    conversations = Conversation.objects.filter(item=target_item).filter(members__in=[request.user.id])

    if conversations:
        return redirect('communication:detail',pk=conversations.first().id)
        

    if request.method == 'POST':
        form = ConversationForm(request.POST)
        if form.is_valid():
            new_conversation = Conversation.objects.create(item=target_item)
            new_conversation.members.add(request.user)
            new_conversation.members.add(target_item.created_by)
            new_conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = new_conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationForm()

    return render(request, 'communication/new.html', {'form': form})



@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])

    return render(request,'communication/inbox.html',{'conversations':conversations})

@login_required
def detail(request, pk):
    conversation = Conversation.objects.filter(members__in=[request.user.id]).get(pk=pk)
    if request.method =='POST':
        form=ConversationForm(request.POST)
        if form.is_valid():
            conversation_message=form.save(commit=False)
            conversation_message.conversation=conversation
            conversation_message.created_by= request.user
            conversation_message.save()
            conversation.save()

            return redirect('communication:detail', pk=pk)

        
    else:

        form=ConversationForm()

    return render(request,'communication/detail.html',{'conversation':conversation,'form':form})





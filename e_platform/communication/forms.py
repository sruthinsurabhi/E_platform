from django import forms
from .models import ConversationsMessage

class ConversationForm(forms.ModelForm):
    class Meta:
        model = ConversationsMessage
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control rounded-0',  # Add Bootstrap classes for styling
                'rows': '4',
                'placeholder': 'Enter your message here...',
                'style': 'resize:none;',  # Disable textarea resizing
            })
        }

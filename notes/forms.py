from .models import Note
from django import forms


class postform(forms.ModelForm):
    class Meta:
        model=Note
        fields=['title','content']
        widgets={
            'content': forms.Textarea(attrs={
            'placeholder': 'Write your note here...',
            'rows': 6,
            }),
            'title': forms.TextInput(attrs={
            'placeholder': 'Write your title here...',
            'rows': 2,
            }),
        }

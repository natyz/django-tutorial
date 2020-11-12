from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ["name", "comment_text"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control'}),
        }

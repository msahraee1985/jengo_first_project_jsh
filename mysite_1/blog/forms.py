from django import forms
from .models import comment

class EmailPostForm(forms.Form):
    name = forms.CharField(
        max_length=30,
    )
    to = forms.EmailField()
    comment = forms.CharField(
        required=False,
        widget=forms.Textarea,
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        filds = [
            'name',
            'email',
            'body',
        ]
    


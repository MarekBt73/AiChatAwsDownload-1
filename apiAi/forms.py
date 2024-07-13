from django import forms

class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'w-full p-2 border border-gray-300 rounded-md',
        'rows': 4,
    }))

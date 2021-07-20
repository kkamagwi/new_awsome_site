from django import forms
from .models import UserContacts



class UserContactsForm(forms.ModelForm):

    class Meta:
        model = UserContacts
        fields = ('name', 'phone', 'question')

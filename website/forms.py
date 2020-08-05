from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Snippet ,Contact 

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']



class ContactForms(forms.ModelForm):
    class Meta:
        model = Contact
        fields =['name','phone', 'email','message']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'message':forms.TextInput(attrs={'class':'form-control'}),
        }

    
     


class SnippetForm(forms.ModelForm):
    
    class Meta:
        model = Snippet
        fields = ('name','body')



#< ! -- This is for Email sending Form --->

# class EmailPostForm(forms.Form):
#     name = forms.CharField(max_length=200)
#     email = forms.EmailField()
#     to = forms.EmailField()
#     comments = forms.CharField(required=False, widget=Textarea)





       
     


        
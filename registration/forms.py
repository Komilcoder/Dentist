from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    firstname = forms.CharField(max_length=150 , widget=forms.TextInput(attrs={'class':'form-control'}))
    lastname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'firstname', 'lastname', 'email', 'password1', 'password2')
        widgets ={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),

        }

    # def __init__(self , *args , **kwargs):
    #     super(SignUpForm , self).__init__(*args, **kwargs)

    #     self.fields['username'].widget.attrs['class']='form-control'
    #     self.fields['password1'].widget.attrs['class']='form-control'
    #     self.fields['password2'].widget.attrs['class']='form-control'    
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Registration
from .utils import is_email_valid


class SignUpForm(forms.ModelForm):
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    # firstname = forms.CharField(max_length=150 , widget=forms.TextInput(attrs={'class':'form-control'}))
    # lastname = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Registration
        fields = ('username', 'firstname', 'lastname', 'email', 'password')
        # widgets ={
        #     'username':forms.TextInput(attrs={'class':'form-control'}),
        #     'firstname':forms.TextInput(attrs={'class':'form-control'}),
        #     'lastname':forms.TextInput(attrs={'class':'form-control'}),
        #     'email':forms.EmailInput(attrs={'class':'form-control'}),
        #     'password1':forms.PasswordInput(attrs={'class':'form-control'}),
        #     'password2':forms.PasswordInput(attrs={'class':'form-control'}),

        # }

    def create(self,validated_data):
        username = validated_data['username']
        firstname = validated_data['firstname']
        lastname = validated_data['lastname']
        email = validated_data['email']
        password = validated_data['password']
        query = Registration.objects.create(username=username,firstname=firstname,lastname=lastname,email=email,password=password)
        query.save()
        return query

    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if not email or not password:
            raise ValidationError('Invalid email or password,please check !')
        return email 


class LoginForm(forms.ModelForm):

    class Meta:
        model = Registration
        fields = ('email', 'password')

    def create(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        login  = Registration.objects.create(email=email,password=password)
        login.save()    
        return login


    def validate(self,attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if not email or not password:
            raise ValidationError('Invalid email or password,please check')
        return email


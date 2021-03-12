from django.shortcuts import render
from .forms import SignUpForm,LoginForm
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login


class RegisterView(View):
    form_class = SignUpForm
    template_name = 'registration/register.html'

    def get(self,request, *args, **kwargs):
        form = self.form_class()
        context = {'form':form}
        return render(request,self.template_name,context)

    def post(self,request, *args, **kwargs):
        data = request.POST
        form = self.form_class(data)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request,self.template_name,{'form':form})     

class LoginView(View):
    def post(self,request,*args, **kwargs):
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')
                user = authenticate(email=email,password=password)
                login(request,user)
                return redirect('home')
        else:
            form = LoginForm()
        return render(request,'registration/login.html',{'form':form})

                
                





    




from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import CreateUserForm, ContactForms, SnippetForm
from django.views.generic import TemplateView , ListView,DetailView
from django.core.paginator import Paginator , EmptyPage,PageNotAnInteger
from django.contrib import messages



# --- starting -----this is creating Form
def contact(request):

    if request.method == 'POST':
        form = ContactForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('name')
            messages.success(request , f'Contact published for {username}')
            return redirect('contact')
    else:        
            

        form = ContactForms()
        context = {'forms':form}

    return render(request , 'website/contact.html', context)
    


def snippet_detail(request):

    if request.method == 'POST':
        form = SnippetForm(request.POST) 
        if form.is_valid():
            form.save()
            

    form = SnippetForm()
    context={'forms':form}
    return render(request , 'website/form.html', context)  



# --- ending Form creating




class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(HomeView, self).get_context_data(object_list=object_list, **kwargs) 
        context['services'] = Service.objects.all() 

      
        return context




def contactinfo(request):

    contact = Contact.objects.all()
    context={'contacts':contact}

    return render(request, 'website/contactinfo.html' , context)


def about(request):
    return render(request, 'website/about.html')



class PriceView(ListView):
    template_name = 'website/pricing.html'
    queryset = Price.objects.all()


class PriceDetailView(DetailView):
    queryset = Price.objects.all()
    template_name = 'website/priceInfo.html' 

    def get_context_data(self , **kwargs):
        context = super().get_context_data(**kwargs)
        context['prices'] = Price.objects.all()
        return context   


# ! -- this is pagination -->
        



class ServiceListView(ListView):
    queryset = Service.objects.all()
    template_name = 'website/service.html'


  

class ServiceDetailView(DetailView):
    queryset = Service.objects.all()
    template_name = 'website/service_detail.html'


    def get_context_data(self , **kwargs):
        context = super().get_context_data( **kwargs) 
        context['services'] = Service.objects.all() 

        return context




def appointment(request):

    if request.method == "POST":
        your_name = request.POST['your-name']
        your_phone = request.POST['your-phone']
        your_email = request.POST['your-email']
        your_address = request.POST['your-address']
        your_schedule = request.POST['your-schedule']
        your_time = request.POST['your-time']
        your_message = request.POST['your-message']

        context ={'your_names':your_name, 'your_phones':your_phone , 'your_emails':your_email,'your_addrese':your_address,'your_schedules':your_schedule,'your_times':your_time,'your_messages':your_message}

        return render(request , 'website/appointment.html', context)  
    else:
        return render(request, 'website/home.html')          


def info(request):
    return render(request , 'website/info.html')



def dentistinfo(request):

    return render(request, 'website/dentistinfo.html')    


def blog(request):

    return render(request , 'website/blog.html')    

def blogdetail(request):
    
    return render(request, 'website/blog-details.html')


    
class DoctorListView(ListView):
    template_name = 'website/team.html'
    queryset = Doctor.objects.all()
    paginate_by = 8


class DoctorDetailView(DetailView):
    template_name = 'website/team_detail.html'
    queryset = Doctor.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["doctors"] = Doctor.objects.all()
        return context 


class DentistListView(ListView):
    template_name = 'website/home.html'
    queryset = Dentist.objects.all()


class DentistDetailView(DetailView):
    template_name = 'website/dentist.html'
    queryset = Dentist.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dentists"] = Dentist.objects.all()
        return context    



class AboutDetailView(DetailView):
    template_name = 'website/about_detail.html'
    queryset = Equipment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["equpments"] = Equipment.objects.all()
        return context

# <-- this is Email sending Forms -->

# def post_share(request , post_id):
#     post = get_object_or_404() 

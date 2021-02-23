
from django.urls import path
from .import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('form/' , views.contact , name="form"),
    path('snippet/', views.snippet_detail , name="snipet"),
    path('contact/', views.contact , name="contact"),
  

    path('doctor/', views.DoctorListView.as_view(), name="doctor"),
    path('doctor/<int:pk>/', views.DoctorDetailView.as_view(), name="doctor_detail"),
    
    path('service/' ,views.ServiceListView.as_view(),name='service' ),
    path('service/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    

    path('' , views.DentistListView.as_view(), name="home"),
    path('dentist/<int:pk>/', views.DentistDetailView.as_view(), name="dentist_detail"),
    # path('contact.html/', views.ContactView.as_view() , name="contact"),
    path('contactinfo/', views.contactinfo, name="contactinfo"),
    path('about.html/', views.about , name="about"),
    path('about_detail/<int:pk>/' , views.AboutDetailView.as_view() , name="about_detail"),
    path('pricing.html/', views.PriceView.as_view() , name="pricing"),  
    # path('priceinfo/<int:pk>/', views.PriceDetailView , name="priceInfo"),   
    path('appointment.html/', views.appointment, name="appointment"),


    path('info/' , views.info , name="info"),
    path('dentistinfo/', views.dentistinfo , name="dentistinfo"),
    path('blog-details.html/' , views.blogdetail , name="blog-details.html"),
    path('blog/', views.blog , name="blog"),
    
    

  

]





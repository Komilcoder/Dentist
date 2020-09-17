from django.db import models
from django.utils import timezone
from django.contrib.auth.models  import User


class Snippet(models.Model):
    name = models.CharField(max_length=150)
    body = models.TextField()

    def __str__(self):
        return self.name
    




class Service(models.Model):
    name=models.CharField(max_length=200 , null=True)    
    description = models.TextField()
    items = models.ManyToManyField(to='Item')
    thumbnail = models.ImageField(upload_to='service', null=True)
    cover = models.ImageField(upload_to='service',null=True)
    image1= models.ImageField(upload_to='service', blank=True, null=True)
    image2 = models.ImageField(upload_to='service', blank=True, null=True)

    def __str__(self):
        return self.name



class Item(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title
    

# class Item(models.Model):
#     title = title = models.CharField(max_length=120)

#     def __str__(self):
#         return self.title
        

class Doctor(models.Model):
    name = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='doctors')
    details = models.TextField()
    experience= models.TextField()
    expertize = models.ManyToManyField(to='Expertize' , related_name='doctors')
    twiter = models.CharField(max_length=150 , blank='True', null='True')
    facebook = models.CharField(max_length=150, blank='True', null='True')
    instagram = models.CharField(max_length=150 , blank='True', null='True')

    def __str__(self):
        return self.name
        

class Expertize(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    

        
    


class Price(models.Model):
    
    name = models.CharField(max_length=200 , null=True)
    cost = models.FloatField(max_length=200,null=True)
    text= models.TextField(max_length=850 , null=True)

    def __str__(self):
        return self.name
    




# for contact page
class Contact(models.Model):
    name = models.CharField(max_length=200 , null=True)
    phone = models.CharField(max_length=200)  
    email = models.EmailField(max_length=200 , null=True)
    message = models.TextField(null=True)

    
    def __str__(self):
        return self.name



# for dentist page
class Dentist(models.Model):
    image = models.ImageField(upload_to="doctors")
    name = models.CharField(max_length=150)
    speciality = models.CharField(max_length=200)
    experience = models.TextField()
    phone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, null=True)

    def __str__(self):
        return self.name
    



# start for about page
class Experience(models.Model):
    text = models.TextField()
    image1 = models.ImageField(upload_to="service", blank=True , null=True) 
    image2 = models.ImageField(upload_to="service", blank=True, null=True)

    def __str__(self):
        return self.text


class Equipment(models.Model):
    description = models.TextField()
    image1 = models.ImageField(upload_to="service" , blank=True, null=True)
    image2 = models.ImageField(upload_to="service" , blank=True, null=True)


    def __str__(self):
        return self.description


class Friendly_staff(models.Model):
    staff = models.CharField(max_length=200 , null=True)
    image1 = models.ImageField(upload_to="service", blank=True , null=True)
    image2 = models.ImageField(upload_to="service", blank=True , null=True)

    def __str__(self):
        return self.staff
            
# end about page


# for pricing table , getting data

class Service_name(models.Model):
    name = models.CharField(max_length=200)
    stage = models.CharField(max_length=300)
    price = models.FloatField()

    def __str__(self):
        return self.name
    


        
            
            
          
            
    



from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import FarmerForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Farmer
from django.core.mail import send_mail
# from twilio.rest import TwilioRestClient


class FarmerFormView(View):
    form_class = FarmerForm
    initial = {'key': 'value'}
    template_name = 'app_dairyform/index.html'
    template_post_name = 'app_dairyform/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        #raise NameError(request.__dict__)
        #raise NameError(request.POST['Name'])
        option=request.POST['operation']
        if option == 'edit':
            option = request.POST['operation']
        if option == 'create':
            query = request.POST
            firstname = query['firstname']
            lastname = query['lastname']
            gender = query['gender']
            phone_number = query['contact_number']
            age=query['age']
            model = Farmer.objects.create(FirstName = firstname, LastName = lastname, Gender=gender, ContactNumber=phone_number, Age=age)
            farmers=Farmer.objects.all()
            # model_obj = {'id': model.id, 'FirstName': model.FirstName}
            return render(request, self.template_name, {'create': True, 'farmers': farmers})

        elif option == 'update':
            # raise NameError(request.__dict__)
            id = request.POST['choice']
            farm = Farmer.objects.get(pk=id)
            farm.save()
            # farmers = Farmer.objects.all()
            return render(request, self.template_name, {'update': True, 'farm': farm})

        elif option == 'save':
            id = request.POST['updateid']
            # raise NameError(request.__dict__)
            field = Farmer.objects.get(pk=id)
            query = request.POST
            field.FirstName = query.get('firstname')
            field.LastName = query.get('lastname')
            field.Gender = query.get('gender')
            field.ContactNumber = query.get('contact_number')
            field.Age =  query.get('age')
            field.save()
            # model = Farmer.objects.save(FirstName=firstname, LastName=lastname, Gender=gender, ContactNumber=phone_number, Age=age)
            value=Farmer.objects.all()
            return render(request, self.template_name, {'save': True, 'value':value})

        else :
            # raise NameError(request.__dict__)
            id = request.POST['choice']
            farm = Farmer.objects.get(pk=id)
            farmer = Farmer.objects.all()
            farm.delete()
            return render(request, self.template_name, {'delete': True, 'farmer': farmer})


def home(request):
    return render(request,'app_dairyform/home.html')


def about(request):
    return render(request,'app_dairyform/about.html')


def email(request):
    message = 'hi'
    subject = 'thank you'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['yedla.jyothi95@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
    return render(request,'app_dairyform/response.html')


def response(request):
    return render(request,'app_dairyform/response.html')

def home1(request):
    return render(request,'app_dairyform/home.html')

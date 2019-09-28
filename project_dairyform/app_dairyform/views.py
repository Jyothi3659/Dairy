from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import FarmerForm
from django.core.mail import send_mail
from django.conf import settings
from .models import Farmer


class FarmerFormView(View):
    form_class = FarmerForm
    initial = {'key': 'value'}
    template_name = 'app_dairyform/index.html'
    template_post_name = 'app_dairyform/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        # raise NameError(request.__dict__)
        # raise NameError(request.POST['Name'])
        option=request.POST['operation']
        if option == 'edit':
            query = request.POST
            name = query['name']
            gender = query['gender']
            phone_number = query['contact_number']
            age=query['age']
            model = Farmer.objects.create(Name= name, Gender=gender, ContactNumber=phone_number, Age=age)
            return render(request, self.template_post_name)


def home(request):
    return render(request,'app_dairyform/home.html')


def about(request):
    return render(request,'app_dairyform/about.html')


def email(request):
    return render(request,'app_dairyform/email.html')


def response(request):
    return render(request,'app_dairyform/response.html')
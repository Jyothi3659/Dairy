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
            id = request.POST['choice']
            farm = Farmer.objects.get(pk=id)
            # farmers = Farmer.objects.all()
            return render(request, self.template_name, {'update': True, 'farm': farm})


        else:
            # raise NameError(request.__dict__)
            id = request.POST['choice']
            farm = Farmer.objects.get(pk=id)
            farmer = Farmer.objects.all()
            farm.delete()
            return render(request, self.template_name, {'create': True, 'farmer': farmer})

def home(request):
    return render(request,'app_dairyform/home.html')

def about(request):
    return render(request,'app_dairyform/about.html')

def email(request):
    return render(request,'app_dairyform/email.html')

def response(request):
    return render(request,'app_dairyform/response.html')









  # def update(request, id):
  #               emp = Employee.objects.get(pk=id)
  #               # you can do this for as many fields as you like
  #               # here I asume you had a form with input like <input type="text" name="name"/>
  #               # so it's basically like that for all form fields
  #               emp.name = request.POST.get('name')
  #               emp.save()
  #               return HttpResponse('updated')
# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import FarmerForm
from django.contrib.auth.models import User,auth
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
        #raise NameError(request.__dict__)
        # raise NameError(request.POST['Name'])
        query = request.POST
        name = query['name']
        gender = query['gender']
        phone_number = query['contact_number']
        age=query['age']
        model = Farmer.objects.create(Name= name, Gender=gender, ContactNumber=phone_number, Age=age)
        print(model)
        # return HttpResponseRedirect('self.template_post_name')

        return render(request, self.template_post_name, {'form': model})

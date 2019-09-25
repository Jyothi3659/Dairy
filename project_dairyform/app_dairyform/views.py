# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import FarmerForm


class FarmerFormView(View):
    form_class = FarmerForm
    initial = {'key': 'value'}
    template_name = 'app_dairyform/index.html'
    template_post_name = 'app_dairyform/register.html'

    def get(self, request, *args, **kwargs):

        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('self.template_post_name')

        return render(request, self.template_post_name, {'form': form})

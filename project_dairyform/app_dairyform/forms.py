from django.forms import ModelForm
from .models import Farmer


class FarmerForm(ModelForm):
    class Meta:
        model = Farmer
        fields = ['FirstName', 'LastName', 'Gender', 'ContactNumber', 'Age']
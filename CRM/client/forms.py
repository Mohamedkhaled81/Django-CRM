from django.forms import ModelForm
from .models import Client

class AddClientForm(ModelForm):

    class Meta:
        model = Client
        fields  = [
            'name','email','description',
        ]
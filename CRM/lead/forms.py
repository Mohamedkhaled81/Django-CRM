from django.forms import ModelForm
from .models import Leads

class CreateLead(ModelForm):

    class Meta:
        model = Leads
        fields  = [
            'name','email','description','priority','status'
        ]
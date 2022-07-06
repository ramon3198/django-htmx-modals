from django.forms import ModelForm
from .models import *
class vlanForm(ModelForm):
    class Meta:
        model = vlanModel
        fields = '__all__'
        exclude = ['created_at']
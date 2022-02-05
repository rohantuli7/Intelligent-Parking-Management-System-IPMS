from django import forms
from .models import finedata
from django.utils.translation import ugettext_lazy as _
import string

class number_images(forms.ModelForm):
    class Meta:
        model = finedata
        fields = ('name', 'fine', 'image')
from django import forms
from .models import *
from django.contrib.auth import get_user_model
User = get_user_model()

class PrescriptionForm(forms.ModelForm):

    class Meta:
        model = Prescription
        fields = ('patient', 'symptoms', 'prescription')

    def __init__(self, *args, **kwargs):
        super(PrescriptionForm, self).__init__(*args, **kwargs)
        if self.instance:
            self.fields['patient'].queryset = User.objects.filter(user_type="P")
        

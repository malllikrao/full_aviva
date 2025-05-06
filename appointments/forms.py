# forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        required=True
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        required=True
    )

    class Meta:
        model = Appointment
        fields = ['name', 'email', 'phone', 'service', 'message', 'date', 'time']
#from django import forms
#from .models import Appointment

#class AppointmentForm(forms.ModelForm):
    #class Meta:
        #model = Appointment
        #fields = ['name', 'email', 'phone', 'service', 'date', 'time', 'message']  # ⬅️ Add 'time'
        #widgets = {
           # 'date': forms.DateInput(attrs={'type': 'date'}),
            #'time': forms.TimeInput(attrs={'type': 'time'}),  # ⬅️ Time input widget
        
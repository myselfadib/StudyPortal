from dataclasses import field, fields
from django import forms 
from . models import *

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title','description']
        

class DateInput(forms.DateInput):
    input_type = 'date' 

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ['subject','title','description','due','is_finished']


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100,label='Enter your search')

class TodoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title','is_finished']

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurement = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)        
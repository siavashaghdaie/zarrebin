
from django.forms import ModelForm, widgets
from django import forms

import podcast
from .models import Message, Podcast

class MessageForm(ModelForm):
    #Required_css_class = 'form-fields'
    class Meta:
        model = Message
        fields = '__all__'
        #widgets={
            #'sender' : forms.TextInput(attrs={'id':'send-box'})
        #}
       
class PodcastForm(ModelForm):
    class Meta:
        model = Podcast
        fields = '__all__'
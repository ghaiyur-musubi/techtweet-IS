from django import forms
from django.utils.html import strip_tags
from .models import Tweet
import cloudinary
from cloudinary.forms import CloudinaryFileField



class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'What is on your mind ? ',
                                    'class': 'form-control'
                                }))
    image = CloudinaryFileField(required = False)
    
    class Meta:
        model = Tweet     #Sending Details to body and image 
        exclude = ('user', )
        fields= '__all__'
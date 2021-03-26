from django import forms
from django.utils.html import strip_tags
from .models import Tweet
import cloudinary
from cloudinary.models import CloudinaryField


class TweetForm(forms.ModelForm):
    body = forms.CharField(required=True,
                            widget=forms.widgets.Textarea(
                                attrs={
                                    'placeholder': 'Tweet',
                                    'class': 'form-control'
                                }))
    class Meta:
        model = Tweet
        exclude = ('user', )
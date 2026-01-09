from django import forms
from .models import Reviews
from django.contrib.auth.models import User
# reviews
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields ='__all__'
# User
class UserInfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
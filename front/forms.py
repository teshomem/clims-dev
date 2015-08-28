from django import forms
from front.models import Project, Sample, UserProfile
from django.conf import settings

class UserProfileForm(forms.ModelForm):
        class Meta:
                model = UserProfile

                exclude = ['user'] 

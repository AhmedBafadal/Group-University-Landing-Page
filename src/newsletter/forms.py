from django.core.exceptions import ValidationError
from django import forms

from .models import SignUp

RUSSELL_GROUP = ['bham', 'bristol', 'cam', 'cardiff','dur','ed','exeter','gla','imperial','kcl','leeds','liverpool','lse','manchester','ncl','nottingham',
'ox','qmul','qub','sheffield','southampton','ucl','warwick','york',]

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField()
    



class SignUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email', ]


    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.lower().split("@")
        try:
            domain, extension, c_code = provider.split('.')
        except:
            domain, extension = provider.split('.')

        if not domain in RUSSELL_GROUP:
            raise forms.ValidationError("Please use your Russell Group email.")
        if not extension == "ac":
            raise forms.ValidationError("Please use a valid .ac.uk email address from a Russell Group university.")
        if c_code and c_code != "uk":
            raise forms.ValidationError("Please use a valid .ac.uk email address from a Russell Group university.")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')
		#write validation code.
        return full_name






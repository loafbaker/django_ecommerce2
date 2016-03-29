from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class GuestCheckoutForm(forms.Form):
    email = forms.EmailField()
    email2 = forms.EmailField(label='Verify Email')

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email == email2:
            user_exists = User.objects.filter(email=email2).exists()
            if user_exists:
                raise forms.ValidationError('The email has been registered. Please login instead.')
            return email2
        else:
            raise forms.ValidationError('Please confirm emails are the same.')
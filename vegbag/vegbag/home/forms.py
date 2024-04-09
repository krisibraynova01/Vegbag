from django import forms

class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
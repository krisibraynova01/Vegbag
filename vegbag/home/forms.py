from django import forms

class NewsletterSubscriptionForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)

class AddToCartForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
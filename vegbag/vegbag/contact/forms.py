from django import forms

from vegbag.contact.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'placeholder': 'Message'}),
        }
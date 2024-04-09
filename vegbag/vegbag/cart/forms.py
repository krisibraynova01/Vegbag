from django import forms


class DiscountCodeForm(forms.Form):
    coupon_code = forms.CharField(max_length=100,
                                  widget=forms.TextInput(attrs={'placeholder': 'Enter your coupon code'}))

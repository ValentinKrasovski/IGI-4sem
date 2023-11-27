from django import forms
from .models import FAQ, Review

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'user_name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'text']

class CouponApplyForm(forms.Form):
    code = forms.CharField()
from django import forms
from .models import Reviews


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['comment','rate']
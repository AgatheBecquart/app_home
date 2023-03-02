from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Prediction

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name')
        
class ContactUsForm(forms.Form):
   name = forms.CharField(required=False)
   email = forms.EmailField()
   message = forms.CharField(max_length=1000)

class PredictionForm(forms.ModelForm):
    class Meta:
        model = Prediction
        exclude = ['user', 'predicted_price']
        widgets = {
            'waterfront': forms.RadioSelect(attrs={'class': 'radio'}),
            'view': forms.RadioSelect(attrs={'class': 'radio'}),
            'condition': forms.RadioSelect(attrs={'class': 'radio'}),
            'grade': forms.RadioSelect(attrs={'class': 'quality-note'}),
            'has_basement': forms.RadioSelect(attrs={'class': 'radio'}),
            'was_renovated': forms.RadioSelect(attrs={'class': 'radio'}),
        }


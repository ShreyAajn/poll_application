from django import forms
from .models import user_info


class UserCreationForm(forms.ModelForm):
    class Meta:
        model = user_info
        fields = "__all__"

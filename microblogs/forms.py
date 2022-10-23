from django import forms
from .models import User;

class SignUpForm(forms.ModelForm):
    #allows us to relate form to models
    class Meta:
        # add attribuite model
        model = User;
        # specify what fields we want (otherwise all fields included)
        fields = ['first_name', 'last_name' , 'username', 'email', 'bio']
        widgets = {'bio' :forms.Textarea()} #widget to make bio field look like a text field

    new_password = forms.CharField(label='Password', widget=forms.PasswordInput())
    password_confrimation = forms.CharField(label='Password confirmation',widget=forms.PasswordInput())

#now if we change validation constraints within user models - form changes as well

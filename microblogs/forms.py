from django import forms
from django.core.validators import RegexValidator
from .models import User,Post;

class SignUpForm(forms.ModelForm):
    #allows us to relate form to models
    class Meta:
        # add attribuite model
        model = User;
        # specify what fields we want (otherwise all fields included)
        fields = ['first_name', 'last_name' , 'username', 'email', 'bio']
        widgets = {'bio' :forms.Textarea()} #widget to make bio field look like a text field

    new_password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
        validators=[RegexValidator(
            regex = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).*$',
            message = "Password must contain an uppercase character "
            )
        ]
    )

    password_confirmation = forms.CharField(label='Password confirmation',widget=forms.PasswordInput())

    def clean(self):
        super().clean()
        new_password = self.cleaned_data.get('new_password')
        password_confirmation = self.cleaned_data.get('password_confirmation')
        if new_password != password_confirmation:
            self.add_error('password_confirmation', 'Make sure passwords match!')

    def save(self):
        super().save(commit=False)
        user = User.objects.create_user(
            self.cleaned_data.get('username'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            bio=self.cleaned_data.get('bio'),
            password=self.cleaned_data.get('new_password'),

        )
        return user

class PostForm(forms.ModelForm):

    class Meta:
        model = Post;
        fields = ['text']
        widgets = {'text' :forms.Textarea()} #widget to make bio field look like a text field



#now if we change validation constraints within user models - form changes as well

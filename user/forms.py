from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    # username = forms.CharField(label='username', min_length=5, max_length=150)
    # email = forms.EmailField(label='Email')   
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
    # password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'password2' : 'Confirm Password',
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)


        for name , field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
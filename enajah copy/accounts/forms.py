from django import forms


class UserRegistrationForm(forms.Form):
    username = forms.CharField(
        required=True,
        label = "userName",
        max_length = 100
    )
    email = forms.EmailField(
        required = True,

        label= "Email",
        max_length=200,
    )
    password = forms.CharField(
        required = True,
        label="Password",
        max_length = 32,
        widget = forms.PasswordInput()
    )

class UserLoginForm(forms.Form):
    username = forms.CharField(
        required = True,
        label = "username",
        max_length = 200
    )
    password = forms.CharField(
        required = True,
        label="Password",
        max_length = 32,
        widget = forms.PasswordInput()
    )

from django import forms

from Fruitipedia.profiles.models import ProfileModel


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
        }
        exclude = ('image', 'age')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for key, field in self.fields.items():
            field.label = ""


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('email', 'password',)


class DeleteProfileForm(forms.ModelForm):
    class Meta:
        model = ProfileModel
        fields = '__all__'

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()

        return self.instance

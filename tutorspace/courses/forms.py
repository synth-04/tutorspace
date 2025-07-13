from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, User

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="Nome")
    last_name  = forms.CharField(max_length=30, label="Cognome")
    email      = forms.EmailField(label="Email")

    # Campo dropdown per scegliere la classe
    class_code = forms.ModelChoiceField(
        queryset=Group.objects.filter(profile__selectable=True),
        empty_label="Seleziona la tua classe",
        label="Classe"
    )

    class Meta:
        model  = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
            "class_code",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name  = self.cleaned_data["last_name"]
        user.email      = self.cleaned_data["email"]
        if commit:
            user.save()
            user.groups.add(self.cleaned_data["class_code"])
        return user


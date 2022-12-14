# accounts/forms.py
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.utils.translation import ugettext_lazy as _

from articles.models import Team


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("아이디"),
                "required": "True",
            }
        ),
    )

    email = forms.EmailField(
    label="",
    required=True,
    widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": _("Email address"),
            "required": "True",
            }
        ),
    )
    nickname = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("닉네임"),
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("이름"),
                "required": "True",
            }
        ),
    )
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (
            "username",
            "email",
            "last_name",
            "nickname",
        )

class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(

    required=True,
    widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": _("Email address"),
            "required": "True",
            }
        ),
    )
    nickname = forms.CharField(

        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("닉네임"),
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(

        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": _("이름"),
                "required": "True",
            }
        ),
    )
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = [
            "email",
            "last_name",
            "nickname",
        ]
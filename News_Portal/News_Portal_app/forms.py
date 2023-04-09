from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Post, Author, Category
from django.core.exceptions import ValidationError
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group, User


class PostForm(forms.ModelForm):
    heading = forms.CharField(min_length=5)
    author = Author.objects.all().values('auth__username')
    categories = Category.objects.all().values('cat_name')

    class Meta:
        model = Post
        fields = [
            'heading',
            'author',
            'text',
            'categories'
        ]

    def clean(self):
        cleaned_data = super().clean()
        heading = cleaned_data.get("heading")
        text = cleaned_data.get("text")
        if heading == text:
            raise ValidationError("Описание не должно быть идентично названию.")
        return cleaned_data


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user

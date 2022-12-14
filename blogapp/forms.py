from django import forms
from taggit.forms import TagField
from django import forms
from django.contrib.auth.models import User
from .models import Comment,Post,Profile

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label= 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd= self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match')
        return cd['password2']



class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')



class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=32)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class SearchForm(forms.Form):
    query = forms.CharField()


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','body','status','tags','picture')



###############
from django import forms
import re
from django.core.exceptions import ValidationError


from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Message, UserProfile, School, Groups, Schedule


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Passport Raqam", max_length=9,
                               help_text="Iltimos to'g'ri passport raqamini kiriting", widget=forms.TextInput(
            attrs={'class': 'form-control', 'autofocus': None, 'autocomplete': "off", "placeholder": "AA1234567"}))
    first_name = forms.CharField(label="Ism", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Familiya", widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(label="Active", required=False)
    email = forms.EmailField(label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password1 = forms.CharField(label="Parol",
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password2 = forms.CharField(label="Parolni takrorlash", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_active', 'first_name', 'last_name')
        widgets = {
            'is_active': forms.TextInput(attrs={"class": 'form-control'}),
        }

class StudentRegisterForm(UserCreationForm):
    username = forms.CharField(label="Passport Raqam",max_length=9, help_text="Iltimos to'g'ri passport raqamini kiriting", widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': None, 'autocomplete': "off", "placeholder": "AA1234567"}))
    first_name = forms.CharField(label="Ism", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Familiya", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password2 = forms.CharField(label="Parolni takrorlash", widget=forms.PasswordInput(attrs={'class': 'form-control'}))



    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2')

    def clean_username(self):
        title = self.cleaned_data['username']
        if re.match(r'[A-Z]{2}(?:\d{7})', title):
            return title
        raise ValidationError("Passport seriyasi xato tartibda kiritildi!")


class TeacherRegisterForm(UserCreationForm):
    username = forms.CharField(label="Passport Raqam",max_length=9, help_text="Iltimos to'g'ri passport raqamini kiriting", widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': None, 'autocomplete': "off", "placeholder": "AA1234567"}))
    first_name = forms.CharField(label="Ism", widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label="Familiya", widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_active = forms.BooleanField(label="Active", required=False)
    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': "off"}))
    password2 = forms.CharField(label="Parolni takrorlash", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name',  'is_active')
        widgets = {
            'is_active': forms.TextInput(attrs={"class": 'form-control'}),
        }

    def clean_username(self):
        title = self.cleaned_data['username']
        if re.match(r'[A-Z]{2}(?:\d{7})', title):
            return title
        raise ValidationError("Passport seriyasi xato tartibda kiritildi!")




class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('school',)

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('sinf',)




class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Passport raqam:", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder':"AA1234567"}))
    password = forms.CharField(label="Parol:",
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        # fields = '__all__'
        fields = ['name', 'email', 'content']

        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'email': forms.EmailInput(attrs={"class": 'form-control'}),
            'content': forms.Textarea(attrs={"class": 'form-control md-textarea', "rows":3}),
        }
class DateInput(forms.DateInput):
    input_type = "date"


class SchoolForm(forms.ModelForm):

    class Meta:
        model = School
        fields = ['name', 'address', 'phone', 'contract_num', 'contract_finish', 'status']

        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'address': forms.TextInput(attrs={"class": 'form-control'}),
            'phone': forms.TextInput(attrs={"class": 'form-control'}),
            'contract_num': forms.TextInput(attrs={"class": 'form-control'}),
            'contract_finish': DateInput(),
            'status': forms.CheckboxInput(attrs={"class": 'form-control text-left'}),
        }



class GroupForm(forms.ModelForm):
    # form = GroupTeacherForm
    class Meta:
        model = Groups
        fields = ['name', 'end', 'teacher', 'status']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'end': DateInput(),
            'status': forms.CheckboxInput(attrs={"class": ''}),
        }


class GroupteacherForm(forms.ModelForm):
    # form = GroupTeacherForm
    class Meta:
        model = Groups
        fields = ['name', 'end', 'status']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'end': DateInput(),
            'status': forms.CheckboxInput(attrs={"class": ''}),
        }


class TimeInput(forms.TimeInput):
    input_type = 'time'


class SubjectForm(forms.ModelForm):
    name = forms.CharField(label="Fan nomi", widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': None}))

    class Meta:
        model = Schedule
        fields = ['name', 'begin', 'days']
        widgets = {
            'name': forms.TextInput(attrs={"class": 'form-control'}),
            'days': forms.Select(attrs={"class": 'form-control'}),
            'begin': TimeInput()
        }


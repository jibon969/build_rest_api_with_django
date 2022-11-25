from django import forms
from django.contrib import messages
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.urls import reverse
from django.contrib.auth import authenticate, login, get_user_model
from django.utils.safestring import mark_safe
from .models import EmailActivation
from datetime import date

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        # print('working form')
        request = self.request
        data = self.cleaned_data
        email = data.get("email")
        password = data.get("password")
        qs = User.objects.filter(email=email)
        if qs.exists():
            # user email is registered, check active/
            not_active = qs.filter(is_active=False)
            if not_active.exists():
                # not active, check email activation
                link = reverse("account:resend-activation")
                reconfirm_msg = """Go to <a href='{resend_link}'>
                resend confirmation email</a>.
                """.format(resend_link=link)
                confirm_email = EmailActivation.objects.filter(email=email)
                is_confirmable = confirm_email.confirmable().exists()
                if is_confirmable:
                    msg1 = "Please check your email to confirm your account or " + reconfirm_msg.lower()
                    raise forms.ValidationError(mark_safe(msg1))
                email_confirm_exists = EmailActivation.objects.email_exists(
                    email).exists()
                if email_confirm_exists:
                    msg2 = "Email not confirmed. " + reconfirm_msg
                    raise forms.ValidationError(mark_safe(msg2))
                if not is_confirmable and not email_confirm_exists:
                    raise forms.ValidationError("This user is inactive.")
        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.add_message(request, messages.SUCCESS, 'E-mail or password is incorrect')
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data


class LoginFormContact(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(LoginFormContact, self).__init__(*args, **kwargs)

    def clean(self):
        # print('working form')
        request = self.request
        data = self.cleaned_data
        email = data.get("contact_number")
        password = data.get("password")
        qs = User.objects.filter(email=email)
        if qs.exists():
            # user email is registered, check active/
            not_active = qs.filter(is_active=False)
            if not_active.exists():
                # not active, check email activation
                link = reverse("account:resend-activation")
                reconfirm_msg = """Go to <a href='{resend_link}'>
                resend confirmation email</a>.
                """.format(resend_link=link)
                confirm_email = EmailActivation.objects.filter(email=email)
                is_confirmable = confirm_email.confirmable().exists()
                if is_confirmable:
                    msg1 = "Please check your email to confirm your account or " + reconfirm_msg.lower()
                    raise forms.ValidationError(mark_safe(msg1))
                email_confirm_exists = EmailActivation.objects.email_exists(
                    email).exists()
                if email_confirm_exists:
                    msg2 = "Email not confirmed. " + reconfirm_msg
                    raise forms.ValidationError(mark_safe(msg2))
                if not is_confirmable and not email_confirm_exists:
                    raise forms.ValidationError("This user is inactive.")
        user = authenticate(request, username=email, password=password)
        if user is None:
            messages.add_message(request, messages.SUCCESS, 'E-mail or password is incorrect')
            raise forms.ValidationError("Invalid credentials")
        login(request, user)
        self.user = user
        return data


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
    dob = forms.DateField(input_formats=['%Y-%m-%d'])

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'contact_number', 'gender', 'dob')

    def clean_email(self):
        # print('cleaning mail')
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        # print('cleaning password')
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def clean_dob(self):
        born = self.cleaned_data.get("dob")
        # print(born)
        today = date.today()
        age = today.year - born.year - \
            ((today.month, today.day) < (born.month, born.day))
        # print(age)
        if age < 13:
            raise forms.ValidationError("You Must be 13!")
        return born

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data.get("password"))
        user.is_active = False
        if commit:
            user.save()
        return user


class UserAdminCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'dob', 'gender', 'contact_number')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'dob', 'gender', 'contact_number')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserDetailChangeForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))
    last_name = forms.CharField(label='Last Name', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))
    dob = forms.DateField(input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={"class": 'form-control', 'id': 'datepicker'}))
    contact_number = forms.CharField(label='Contact Number', required=False, widget=forms.TextInput(attrs={"class": 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'dob', 'gender', 'contact_number']

    def clean_dob(self):
        born = self.cleaned_data.get("dob")
        print(born)
        today = date.today()
        age = today.year - born.year - \
            ((today.month, today.day) < (born.month, born.day))
        print(age)
        if age < 13:
            raise forms.ValidationError("You Must be 13!")
        return born


class ReactivateEmailForm(forms.Form):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = EmailActivation.objects.email_exists(email)
        if not qs.exists():
            register_link = reverse("account:register")
            msg = """This email does not exists, would you like to <a href="{link}">register</a>?
            """.format(link=register_link)
            raise forms.ValidationError(mark_safe(msg))
        return email

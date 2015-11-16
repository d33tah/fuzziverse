from django.contrib.auth import authenticate, get_user_model
User = get_user_model()

from django.utils.translation import ugettext_lazy as _
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.sites import AdminSite
from django.contrib import admin


class UserAdminAuthenticationForm(AuthenticationForm):
    """
    Same as Django's AdminAuthenticationForm but allows to login
    any user who is not staff.
    """
    this_is_the_login_form = forms.BooleanField(widget=forms.HiddenInput,
                                initial=1,
                                error_messages={'required': _(
                                "Please log in again, because your session has"
                                " expired.")})

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError("Login error")
            else:
                self.confirm_login_allowed(self.user_cache)
        return self.cleaned_data


class UserAdmin(AdminSite):

    login_form = UserAdminAuthenticationForm

    def has_permission(self, request):
        """
        Removed check for is_staff.
        """
        return request.user.is_active


user_admin_site = UserAdmin(name='usersadmin')



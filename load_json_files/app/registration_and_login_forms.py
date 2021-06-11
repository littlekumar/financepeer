from allauth.account.views import *
from django.shortcuts import resolve_url

class Signup_View(SignupView):
    template_name = "account/registration."+ app_settings.TEMPLATE_EXTENSION
    form_class = SignupForm
    redirect_field_name = "next"
    success_url = '/login/'

from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):
        # Add your own processing here.
        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)

class Login_View(LoginView):
    form_class = LoginForm
    template_name = "account/log_in." + app_settings.TEMPLATE_EXTENSION
    redirect_field_name = "next"
    def get_success_url(self):
        return resolve_url('homepage')

class Confirm_EmailView(ConfirmEmailView):
    def get_redirect_url(self):
        return get_adapter(self.request).get_email_confirmation_redirect_url(
            'mail_verifiedsss'
        )

class Logout_View(LogoutView):
    next_page = None
    template_name = "account/log_out." + app_settings.TEMPLATE_EXTENSION
    # template_name = "account/logout." + app_settings.TEMPLATE_EXTENSION
    extra_context = None

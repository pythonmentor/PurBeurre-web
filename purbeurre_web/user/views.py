from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from .admin import UserCreationForm


class SignUp(CreateView):
    """
    This view is used to create a user account.
    """
    form_class = UserCreationForm
    success_url = reverse_lazy('index')
    template_name = 'signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get('email'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


@method_decorator(login_required, name='dispatch')
class Account(TemplateView):
    """
    This view is used to display the user account.
    User must be logged in to access this view.
    If the user is not logged in and tries to access this page,
    he will be redirected to the login page.
    """
    template_name = 'account.html'

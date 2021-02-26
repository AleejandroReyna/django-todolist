from django.contrib.auth.views import LoginView as AuthLoginView, LogoutView as AuthLogoutView
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages


class HomeView(TemplateView):
    template_name = 'pages/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/dashboard.html'
    login_url = reverse_lazy('pages:login')


class SignUpView(CreateView):
    model = User
    form_class = UserCreationForm
    template_name = 'pages/signup.html'

    def get_success_url(self):
        return reverse_lazy('pages:login')


class LogInView(AuthLoginView):
    template_name = 'pages/login.html'

    def get_success_url(self):
        messages.success(self.request, "Has iniciado sesión.")
        return super(LogInView, self).get_success_url()

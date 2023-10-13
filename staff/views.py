from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import generic
from .forms import AdminUserCreationForm

class AdminUserRegistrationView(generic.CreateView):
    form_class = AdminUserCreationForm
    template_name = 'adminregistration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/dashboard/')

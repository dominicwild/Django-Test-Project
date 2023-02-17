from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView


class UserRegistrationView(FormView):
    template_name = "recipe_site/registration.html"
    form_class = UserCreationForm
    success_url = reverse_lazy('recipe_site:home')

    # def post(self, request, *args, **kwargs):
    #     super().post(request, *args, **kwargs)
    #
    # def form_valid(self, form):
    #     super().form_valid()
    #     form.is_valid()
    #     return HttpResponseRedirect(self.get_success_url())

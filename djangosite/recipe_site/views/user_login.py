from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect


class UserLoginView(LoginView):
    template_name = "recipe_site/login.html"

    def post(self, request, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            user = authenticate(request, username=form_data["username"], password=form_data["password"])

            if user is not None:
                login(request, user)
                return redirect("recipe_site:home")

        return render(request, self.template_name, {"form": form})

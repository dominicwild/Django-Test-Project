from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "recipe_site/home.html"

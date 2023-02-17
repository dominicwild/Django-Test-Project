from django.views.generic import TemplateView


class RecipeIndexView(TemplateView):
    template_name = "recipe_site/recipes.html"

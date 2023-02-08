from django.urls import path

from recipe_site.views.login_view import LoginView

app_name = 'recipe_site'
urlpatterns = [
    path('login/', LoginView.as_view(), name='index'),
]

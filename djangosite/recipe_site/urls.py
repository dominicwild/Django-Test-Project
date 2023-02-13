from django.urls import path

from recipe_site.views.user_login_view import UserLoginView

app_name = 'recipe_site'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='index'),
]

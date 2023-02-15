from django.urls import path

from recipe_site.views.home import HomeView
from recipe_site.views.user_login import UserLoginView
from recipe_site.views.user_logout import UserLogoutView

app_name = 'recipe_site'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path("home/", HomeView.as_view(), name="home")
]

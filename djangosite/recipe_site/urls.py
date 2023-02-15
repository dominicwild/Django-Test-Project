from django.urls import path

from recipe_site.views.user_login_view import UserLoginView
from recipe_site.views.user_logout_view import UserLogoutView

app_name = 'recipe_site'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
]

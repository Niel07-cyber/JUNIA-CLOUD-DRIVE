from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
     path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(next_page='/accounts/login/'), name='logout'),
]
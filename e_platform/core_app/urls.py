from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .forms import LoginForm
from django.contrib.auth.views import LogoutView

app_name = "core_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core_app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')  # Add this line for the logout view
]

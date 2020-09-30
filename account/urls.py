from django.urls import path
from .views import signup
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
         
         path('register/', signup, name='register'),
         path('login/',LoginView.as_view(template_name='account/login.html'), name= 'login'),
         path('logout/', LogoutView.as_view(template_name= 'account/logout'), name= 'logout'),

]